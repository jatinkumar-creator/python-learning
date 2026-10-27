import json
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent / "scratch"
SCRATCH.mkdir(exist_ok=True)
FILE = SCRATCH / "library.json"

class Book:
    def __init__(self, title, author, price, available=True):
        self.title, self.author, self.price, self.available = title, author, price, available

    def to_dict(self):
        return {"title": self.title, "author": self.author,
                "price": self.price, "available": self.available}

    @classmethod
    def from_dict(cls, d):
        return cls(d["title"], d["author"], d["price"], d["available"])

    def __repr__(self):
        return f"Book({self.title!r}, available={self.available})"

class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def add(self, book):
        self.books.append(book)

    def checkout(self, title):
        for b in self.books:
            if b.title == title and b.available:
                b.available = False
                return True
        return False

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)

    @classmethod
    def load(cls, path):
        try:
            with open(path, encoding="utf-8") as f:
                return cls([Book.from_dict(d) for d in json.load(f)])
        except FileNotFoundError:
            return cls()

lib = Library.load(FILE)
if not lib.books:
    lib.add(Book("Python Basics", "A. Kumar", 450))
    lib.add(Book("Advanced Python", "R. Singh", 650))
print("Loaded:", lib.books)
print("Checkout:", lib.checkout("Python Basics"), lib.checkout("Python Basics"))
lib.save(FILE)
print(FILE.read_text(encoding="utf-8"))



#(objects and files together)