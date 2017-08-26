def tokenizer(text):
    return text.split()

def tokenizer_porter(text):
#     return [porter.stem(word) for word in text.split()]
    for word in text.split():
        try:
            return porter.stem(word)
        except Exception:
            return word