valid_words = ['cat', 'mat', 'sat', 'the']
document = """The cat sat on the mat"""
def spellcheck(document, valid_words):
    valid_set = set(valid_words)
    new_set = set()
    words = document.split()
    for word in words:
        word = word.lower()
        if word not in valid_set:
            new_set.add(word)
    return new_set
