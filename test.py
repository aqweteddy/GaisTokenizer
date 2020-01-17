from gaisTokenizer import Tokenizer


gt = Tokenizer()
text = '這裡我們以 GET 下載 Google 的網頁後，將結果儲存於 r 這個變數中，首先確認一下從伺服器傳回的狀態碼：# 伺服器回應的狀態碼'

r = gt.extract_keywords(text)
print(r) # list[str]
# ['伺服器', '網頁', '下載']

r = gt.tokenize(text)
print(r) # list[str]
# '這裡', '我們', '以', 'GET', '下載', 'Google', '的', '網頁', '後', '，', '將', '結果', '儲存', '於', 'r', '這個', '變數', '中', '，', '首先', '確認', '一下', '從', '伺服器', '傳回', '的', '狀態', '碼', '：']

r = gt.tokenize(f'楊幼蘭{text}', unk_token_idx=True)
print(r) # list[str]
# '這裡', '我們', '以', 'GET', '下載', 'Google', '的', '網頁', '後', '，', '將', '結果', '儲存', '於', 'r', '這個', '變數', '中', '，', '首先', '確認', '一下', '從', '伺服器', '傳回', '的', '狀態', '碼', '：']
# [0]

r = gt.get_words_keywords(text)
print(r) # (words: list, keywords: list)
# (['這裡', '我們', '以', 'GET', '下載', 'Google', '的', '網頁', '後', '，', '將', '結果', '儲存', '於', 'r', '這個', '變數', '中', '，', '首先', '確認', '一下', '從', '伺服器', '傳回', '的', '狀態', '碼', '：'], ['伺服器', '網頁', '下載'])