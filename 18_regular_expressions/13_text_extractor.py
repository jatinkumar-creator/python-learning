import re

TEXT = """
Contact Asha at asha.k@example.com or ravi_87@shop.co.in.
Call +91 98765 43210, 9123456780 or (011) 2345-6789.
Meeting on 2026-10-27 and again on 03/11/2026, budget Rs. 12,500.50 or INR 3,000.
Docs: https://docs.example.com/guide?id=7 and http://old.example.org.
Tags: #python #regex101 #AI_tools
"""

PATTERNS = {
    "e-mails":    r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+",
    "mobiles":    r"(?:\+91[\s-]?)?[6-9]\d{4}[\s-]?\d{5}",
    "ISO dates":  r"\b\d{4}-\d{2}-\d{2}\b",
    "d/m/y":      r"\b\d{2}/\d{2}/\d{4}\b",
    "amounts":    r"(?:Rs\.?|INR)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
    "hashtags":   r"#\w+",
}

for label, pattern in PATTERNS.items():
    print(f"{label:<10}{re.findall(pattern, TEXT)}")

urls = [u.rstrip(".,;)") for u in re.findall(r"https?://\S+", TEXT)]
print(f"{'urls':<10}{urls}")

amounts = re.findall(r"(?:Rs\.?|INR)\s?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)", TEXT)
print("total:", sum(float(a.replace(",", "")) for a in amounts))