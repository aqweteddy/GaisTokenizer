# GaisTokenizer Simple API

## install

```
pip install git+https://github.com/aqweteddy/GaisTokenizer.git@master
```

## Usage

* 可參考 test.py

### __init__

```python
from gaisTokenizer import Tokenizer
gt = Tokenizer()
```

### 斷詞

```python
gt.tokenize('sentence')
gt.tokenize('sentence', unk_token_idx=True) # return both words, unknown word index
```

### keyword

```python
gt.extract_keywords(text)
```