from typing import List, Tuple

import requests
import logging


class Tokenizer:
    BASE_URL = 'http://gaisdb.ccu.edu.tw:5721/api/segment?content='

    def __init__(self, log_level :str='INFO'):
        self.log = logging.getLogger('GaisTokenizer')
        self.log.setLevel(logging.getLevelName(log_level))
        self.tokenize('.')
    
    def __send_request(self, text: str):
        resp = requests.get(f'{self.BASE_URL}{text}')
        if resp.status_code != 200:
            self.log.error(f'Server Error {resp.status_code}')
        else:
            self.log.info(f'OK!')

        return resp.json()
    
    def tokenize(self, text: str) -> List[str]:
        result = self.__send_request(text)
        return result['recs']
    
    def extract_keywords(self, text: str) -> List[str]:
        result = self.__send_request(text)['Keyterms']
        return [word.strip()for word in result.split(',') if word.strip()]
    
    def get_words_keywords(self, text: str) -> Tuple[List[str]]:
        result = self.__send_request(text)
        words = result['recs']
        keywords = [word.strip()for word in result['Keyterms'].split(',') if word.strip()]
        return words, keywords
    
   