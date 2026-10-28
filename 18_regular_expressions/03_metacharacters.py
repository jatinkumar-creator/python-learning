import re

def show(pattern, text, flags=0):
    print(f"{pattern:<30}{text!r:<32}{re.findall(pattern, text, flags)}")

print("--- . matches anything except a newline ---")
show(r"c.t", "cat cot c-t c\nt ct")
show(r"c.t", "cat cot c-t c\nt ct", re.DOTALL)

print("\n--- ^ and $ ---")
show(r"^\w+", "one two\nthree four")
show(r"^\w+", "one two\nthree four", re.M)
show(r"\w+$", "one two\nthree four")
show(r"\w+$", "one two\nthree four", re.M)

print("\n--- * + ? {} ---")
show(r"ab*", "a ab abb abbb")
show(r"ab+", "a ab abb abbb")
show(r"colou?r", "color colour colouur")
show(r"\d{3}", "12 123 1234")
show(r"\d{2,3}", "1 12 123 1234")
show(r"\d{2,}", "1 12 123456")

print("\n--- [] sets ---")
show(r"[aeiou]", "education")
show(r"[a-c]+", "abcdcba xyz")
show(r"[^0-9]+", "ab12cd3")
show(r"[.*+?]", "a.b*c+d?e")                  # metacharacters are literal inside []
show(r"[\d.]+", "v3.14.15 x")

print("\n--- | and () ---")
show(r"cat|dog", "cat dog bird")
show(r"gr(a|e)y", "gray grey")                # findall returns the GROUP
show(r"gr(?:a|e)y", "gray grey")              # (?: ) groups without capturing
show(r"gr[ae]y", "gray grey")
show(r"a|ab", "ab")                           # the FIRST alternative that works wins...
show(r"ab|a", "ab")                           # ...not the longest

print("\n--- escaping ---")
show(r"a.c", "a.c abc")
show(r"a\.c", "a.c abc")
show(r"\$\d+", "cost $50 and $7")

print("\n--- empty matches ---")
show(r"x*", "axb")                            # matches the empty string at several positions