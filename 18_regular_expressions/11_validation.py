import re
from datetime import date

RULES = {
    "PIN code":   (r"[1-9]\d{5}", ["110001", "011001", "11000", "1100011"]),
    "Mobile":     (r"(?:\+91[\s-]?)?[6-9]\d{9}", ["9876543210", "+91 9876543210", "+91-9876543210", "5876543210", "98765"]),
    "PAN":        (r"[A-Z]{5}\d{4}[A-Z]", ["ABCDE1234F", "abcde1234f", "ABCD12345F"]),
    "24h time":   (r"(?:[01]\d|2[0-3]):[0-5]\d", ["09:30", "23:59", "24:00", "9:30"]),
    "Hex colour": (r"#(?:[0-9a-fA-F]{3}){1,2}", ["#fff", "#1A2b3C", "#12345", "fff"]),
    "Username":   (r"[A-Za-z][A-Za-z0-9_]{2,15}", ["asha_28", "9asha", "ab", "a" * 17]),
    "E-mail":     (r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", ["asha.k@example.com", "a@x.co.in", "a@b", "@x.com", "a b@x.com"]),
}

for name, (pattern, samples) in RULES.items():
    compiled = re.compile(pattern)
    print(f"\n{name}   {pattern}")
    for sample in samples:
        verdict = "valid" if compiled.fullmatch(sample) else "invalid"
        print(f"  {sample[:24]!r:<28}{verdict}")

# A pattern cannot know the calendar: finish the job in code
DATE = re.compile(r"(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])")

def valid_date(text):
    m = DATE.fullmatch(text)
    if not m:
        return False
    try:
        date(*map(int, m.groups()))
    except ValueError:
        return False
    return True

print()
for t in ("2026-10-27", "2026-02-30", "2026-13-01", "2024-02-29", "2025-02-29"):
    print(f"{t:<12}{valid_date(t)}")

# Same idea for ranges: capture, then compare numbers
def valid_ipv4(text):
    m = re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", text)
    return bool(m) and all(int(part) <= 255 for part in m.groups())

print()
for ip in ("192.168.1.1", "256.1.1.1", "1.2.3", "10.0.0.255"):
    print(f"{ip:<14}{valid_ipv4(ip)}")