class Address:
    def __init__(self, city, pin):
        self.city, self.pin = city, pin

    def __str__(self):
        return f"{self.city} - {self.pin}"

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address              # a Person HAS an Address

    def __str__(self):
        return f"{self.name}, {self.address}"

home = Address("Delhi", "110001")
p1 = Person("Asha", home)
p2 = Person("Ravi", home)                   # two people share one Address object
print(p1)
home.city = "Noida"
print(p1, "|", p2)                          # both changed

class Book:
    def __init__(self, title, author, price):
        self.title, self.author, self.price = title, author, price

class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def find(self, text):
        return [b for b in self.books if text.lower() in b.title.lower()]

    def total_value(self):
        return sum(b.price for b in self.books)

lib = Library()
lib.add(Book("Python Basics", "A. Kumar", 450))
lib.add(Book("Advanced Python", "R. Singh", 650))
lib.add(Book("Cooking 101", "M. Rao", 300))
print([b.title for b in lib.find("python")])
print(lib.total_value())