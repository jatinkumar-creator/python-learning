import json
import secrets
import string
from collections import Counter
from datetime import date, timedelta

from toolkit import is_palindrome, slugify
from toolkit.data.stats import mean, word_counts

# 1. A secure password generator (use secrets, not random, for passwords)
def make_password(length=12):
    alphabet = string.ascii_letters + string.digits + "!@#$%"
    return "".join(secrets.choice(alphabet) for _ in range(length))

print(make_password(), make_password(16))

# 2. Age and days lived
born = date.fromisoformat(input("Birth date (YYYY-MM-DD): "))
today = date.today()
age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
print(f"Age: {age} years, {(today - born).days:,} days old")

# 3. Deadline calculator
due = today + timedelta(days=45)
print("45 days from today:", due.strftime("%A, %d %B %Y"))

# 4. JSON round trip, as strings (file handling comes next)
profile = {"name": "Asha", "skills": ["python", "sql"], "active": True, "manager": None}
text = json.dumps(profile, indent=2)
print(text)
back = json.loads(text)
print(back == profile, back["manager"] is None)

# 5. Using your own package
sentence = "A man, a plan, a canal: Panama"
print(is_palindrome(sentence), slugify(sentence))
print(word_counts("the cat and the hat and the bat").most_common(2))
print(mean([80, 90, 100]))