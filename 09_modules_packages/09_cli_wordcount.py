import argparse
import string
from collections import Counter

parser = argparse.ArgumentParser(description="Count the most common words in some text.")
parser.add_argument("text", help="the text to analyse (put it in quotes)")
parser.add_argument("--top", type=int, default=3, help="how many words to show")
parser.add_argument("--min-length", type=int, default=1, help="ignore shorter words")
args = parser.parse_args()

words = args.text.lower().translate(str.maketrans("", "", string.punctuation)).split()
words = [w for w in words if len(w) >= args.min_length]

for word, count in Counter(words).most_common(args.top):
    print(f"{word:<12}{count}")