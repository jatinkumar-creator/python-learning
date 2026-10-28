import re

RULES = [
    ("email",   r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+",     "[EMAIL]"),
    ("PAN",     r"\b[A-Z]{5}\d{4}[A-Z]\b",           "[PAN]"),
    ("card",    r"\b(?:\d{4}[ -]?){3}(\d{4})\b",     r"**** **** **** \1"),
    ("Aadhaar", r"\b\d{4}\s\d{4}\s\d{4}\b",          "[AADHAAR]"),     # AFTER card: a card starts with 12 such digits
    ("mobile",  r"(?:\+91[\s-]?)?\b[6-9]\d{9}\b",    "[PHONE]"),
]

def redact(text):
    report = {}
    for name, pattern, replacement in RULES:
        text, count = re.subn(pattern, replacement, text)
        report[name] = count
    return text, report

SAMPLE = ("Asha (asha.k@example.com, +91 9876543210) paid with card 4111 1111 1111 1111; "
          "PAN ABCDE1234F; Aadhaar 1234 5678 9012; alternate mobile 9123456780.")

clean, report = redact(SAMPLE)
print(clean)
print(report)