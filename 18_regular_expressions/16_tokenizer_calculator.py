import re

TOKEN = re.compile(r"""
    \s*(?:
        (?P<NUMBER>\d+(?:\.\d+)?)
      | (?P<OP>\*\*|[-+*/()])
      | (?P<BAD>.)
    )
""", re.X)

def tokenize(text):
    tokens = []
    for m in TOKEN.finditer(text.strip()):
        kind = m.lastgroup                       # the name of the group that matched
        value = m.group(kind)
        if kind == "BAD":
            raise ValueError(f"unexpected character {value!r} at position {m.start(kind)}")
        tokens.append((kind, value))
    return tokens

class Parser:
    """expr  := term (('+'|'-') term)*
       term  := unary (('*'|'/') unary)*
       unary := '-' unary | power
       power := atom ('**' unary)?
       atom  := NUMBER | '(' expr ')'"""

    def __init__(self, tokens):
        self.tokens, self.i = tokens, 0

    def peek(self):
        return self.tokens[self.i][1] if self.i < len(self.tokens) else None

    def take(self):
        token = self.tokens[self.i]
        self.i += 1
        return token

    def parse(self):
        value = self.expr()
        if self.peek() is not None:
            raise ValueError(f"unexpected {self.peek()!r}")
        return value

    def expr(self):
        value = self.term()
        while self.peek() in ("+", "-"):
            op = self.take()[1]
            right = self.term()
            value = value + right if op == "+" else value - right
        return value

    def term(self):
        value = self.unary()
        while self.peek() in ("*", "/"):
            op = self.take()[1]
            right = self.unary()
            if op == "/" and right == 0:
                raise ZeroDivisionError("division by zero")
            value = value * right if op == "*" else value / right
        return value

    def unary(self):
        if self.peek() == "-":
            self.take()
            return -self.unary()
        return self.power()

    def power(self):
        base = self.atom()
        if self.peek() == "**":
            self.take()
            return base ** self.unary()          # right-associative, like Python
        return base

    def atom(self):
        if self.peek() is None:
            raise ValueError("unexpected end of expression")
        kind, value = self.take()
        if kind == "NUMBER":
            return float(value)
        if value == "(":
            inner = self.expr()
            if self.peek() != ")":
                raise ValueError("missing closing parenthesis")
            self.take()
            return inner
        raise ValueError(f"unexpected {value!r}")

def calculate(text):
    return Parser(tokenize(text)).parse()

TESTS = ["1 + 2 * 3", "(1 + 2) * 3", "2 ** 3 ** 2", "-2 ** 2", "2 ** -1", "10 / 4",
         "2 * (3 + 4) - 5", "1 / 0", "2 +", "3 $ 4", "(1 + 2", "1 2", ""]
for expr in TESTS:
    try:
        print(f"{expr!r:<20}= {calculate(expr):g}")
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        print(f"{expr!r:<20}error: {type(e).__name__}: {e}")

while True:
    text = input("calc> ").strip()
    if text.lower() in {"q", "quit"}:
        break
    try:
        print(f"{calculate(text):g}")
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        print("Error:", e)