import string
from itertools import groupby

# 1. Palindrome, ignoring case and punctuation
s = "A man, a plan, a canal: Panama"
clean = "".join(ch.lower() for ch in s if ch.isalnum())
print("Palindrome" if clean == clean[::-1] else "Not a palindrome")

# 2. Vowels and consonants
text = "Hello World"
low = text.lower()
vowels = sum(1 for ch in low if ch in "aeiou")
consonants = sum(1 for ch in low if ch.isalpha() and ch not in "aeiou")
print(vowels, consonants)                      # 3 7

# 3. Word frequency, ignoring case and punctuation
sentence = "Hello, hello! How are you? You look great."
words = sentence.lower().translate(str.maketrans("", "", string.punctuation)).split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# 4. Anagram check
a, b = "Listen", "Silent"
print(sorted(a.lower()) == sorted(b.lower()))

# 5. Longest word
print(max("Python makes data handling simple".split(), key=len))

# 6. Caesar cipher
def caesar(text, shift):
    out = []
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base = ord("A") if ch.isupper() else ord("a")
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)

secret = caesar("Hello, World!", 3)
print(secret, caesar(secret, -3))

# 7. Run-length encoding
raw = "aaabbc"
print("".join(f"{ch}{len(list(g))}" for ch, g in groupby(raw)))

# 8. Mask a card number
card = "1234567812345678"
print("*" * (len(card) - 4) + card[-4:])

# 9. Remove duplicate characters, keeping the first occurrence
print("".join(dict.fromkeys("programming")))

# 10. Reverse the word order, then each word
phrase = "Python is fun"
print(" ".join(phrase.split()[::-1]))
print(" ".join(w[::-1] for w in phrase.split()))