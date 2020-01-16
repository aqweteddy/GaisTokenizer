# GaisTokenizer Simple API

## install

```
pip install git@https://github.com/aqweteddy/GaisTokenizer.git@master
```

## Usage

* 可參考 test.py

### __init__

```python
gt = GaisTokenizer()
```

### 斷詞

```python
gt.tokenize('sentence')
```

### keyword

```python
gt.get_words_keywords(text)
```