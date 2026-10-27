# Bad: a Stack that IS-A list inherits every list method, even ones that break a stack
class BadStack(list):
    def push(self, x):
        self.append(x)

s = BadStack()
s.push(1)
s.push(2)
s.insert(0, 99)                             # a stack should never allow this
s.sort()
print(s)

# Better: a Stack that HAS-A list exposes only what a stack should
class Stack:
    def __init__(self):
        self._items = []

    def push(self, x):
        self._items.append(x)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        return self._items[-1] if self._items else None

    def __len__(self):
        return len(self._items)

st = Stack()
st.push(1)
st.push(2)
print(st.pop(), st.peek(), len(st))
print(hasattr(st, "insert"), hasattr(s, "insert"))

# Another common mistake: an override that changes the signature breaks polymorphism
class Notifier:
    def send(self, message):
        return f"Sending: {message}"

class SmsNotifier(Notifier):
    def send(self, message, phone):         # an extra REQUIRED argument
        return f"SMS to {phone}: {message}"

for n in (Notifier(), SmsNotifier()):
    try:
        print(n.send("hello"))
    except TypeError as e:
        print(type(n).__name__, "-> TypeError:", e)