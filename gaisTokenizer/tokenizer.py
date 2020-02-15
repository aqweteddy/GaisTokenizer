from typing import List, Tuple

import requests
from urllib.parse import urlencode


class Tokenizer:
    BASE_URL = 'http://gaisdb.ccu.edu.tw:5721/api/segment?'

    def __init__(self, token=None):
        self.token = token
        self.tokenize('.')

    def __send_request(self, text: str):
        args = urlencode({'token': self.token, 'content': text}
                         if self.token else {'content': text})
        url = f'{self.BASE_URL}{args}'
        try:
            resp = requests.get(url)
            if resp.status_code != 200:
                print(f'Server Error {resp.status_code}')

            return resp.json()
        except json.decoder.JSONDecodeError:
            print(f'JSON Error {resp.status_code}')
            return ''
    def tokenize(self, text: str, unk_token_idx: bool = False) -> List[str]:
        """
        text: text to tokenize
        unk_index[bool]: if true, return word not in dictionary
        """
        pos_start = 0
        result = []
        sep_len = 800
        while len(text[pos_start:]) > sep_len:
            tmp = self.__send_request(text[pos_start:pos_start+sep_len])
            result.extend(tmp['recs'])
            pos_start += sep_len

        # remove * and process new word mark
        def unk_filter(word): return word[0] == '*' and len(word) > 1

        if unk_token_idx:
            unk_idx = [idx for idx, word in enumerate(
                result) if unk_filter(word)]
        result = [word[1:] if unk_filter(word) else word for word in result]

        return (result, unk_idx) if unk_token_idx else result

    def extract_keywords(self, text: str) -> List[str]:
        result = self.__send_request(text)['Keyterms']
        return [word.strip()for word in result.split(',') if word.strip()]

    def get_words_keywords(self, text: str) -> Tuple[List[str]]:
        result = self.__send_request(text)
        words = result['recs']
        keywords = [word.strip()
                    for word in result['Keyterms'].split(',') if word.strip()]
        return words, keywords
