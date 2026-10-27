import string
from functools import reduce

def clean_words(text):
    return text.lower().translate(str.maketrans("", "", string.punctuation)).split()

def word_frequency(words):
    return reduce(lambda acc, w: {**acc, w: acc.get(w, 0) + 1}, words, {})

def longest_word(words):
    return max(words, key=len) if words else None

def has_digit(text):
    return any(c.isdigit() for c in text)

def is_all_alpha(words):
    return all(w.isalpha() for w in words)

def analyse(text, *checks):
    words = clean_words(text)
    return {check.__name__: check(words) for check in checks}

sample = "Hello, hello! Python is fun, and Python is powerful."
print(analyse(sample, word_frequency, longest_word, is_all_alpha))
print(has_digit("abc1"), has_digit("abc"))