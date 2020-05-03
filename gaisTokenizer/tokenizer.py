from typing import List, Tuple

import json
import traceback

import asyncio
import aiohttp
from urllib.parse import urlencode


class Tokenizer:
    BASE_URL = 'http://gaisdb.ccu.edu.tw:5721/api/segment?'

    def __init__(self, token=None, max_cut=100):
        self.token = token
        self.max_cut = max_cut
        self.loop = asyncio.get_event_loop()
        self.tokenize('.')

    async def __send_req(self, session, text):
        args = urlencode({'token': self.token, 'content': text}
                                    if self.token else {'content': text})
        url = f'{self.BASE_URL}{args}'
        try:
            async with session.get(url) as resp:
                js = await resp.json()
                if resp.status != 200:
                    return None
        except Exception as e:
            # print(resp.status)
            traceback.print_exc()
            return None
        
        return js

    async def __send_request(self, text: str):
        pos_start = 0
        tasks = []

        async with aiohttp.ClientSession() as session:
            while len(text[pos_start:]) > self.max_cut:
                tasks.append(asyncio.create_task(self.__send_req(session, text[pos_start:pos_start+self.max_cut])))
                pos_start += self.max_cut

            if text[pos_start:]:
                tasks.append(asyncio.create_task(self.__send_req(session, text[pos_start:pos_start+self.max_cut])))

            result = await asyncio.gather(*tasks)
        recs, keyterms = [], []
        for r in result:
            try:
                recs.extend(r['recs'])
                keyterms.extend(r['Keyterms'])
            except Exception:
                traceback.print_exc()
        
        return recs, keyterms


    def tokenize(self, text: str, unk_token_idx: bool = False) -> List[str]:
        """
        text: text to tokenize
        unk_index[bool]: if true, return word not in dictionary
        """

        # remove * and process new word mark
        result, _ = self.loop.run_until_complete(self.__send_request(text))
        def unk_filter(word): return word[0] == '*' and len(word) > 1

        if unk_token_idx:
            unk_idx = [idx for idx, word in enumerate(
                result) if unk_filter(word)]
        result = [word[1:] if unk_filter(word) else word for word in result]

        return (result, unk_idx) if unk_token_idx else result

    def extract_keywords(self, text: str) -> List[str]:
        _, result = self.loop.run_until_complete(self.__send_request(text))
        return [word.strip() for word in result if word.strip()]
