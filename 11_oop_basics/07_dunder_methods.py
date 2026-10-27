class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):                      # for developers: unambiguous
        return f"Vector({self.x}, {self.y})"

    def __str__(self):                       # for users: readable
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):                      # needed if you define __eq__ and want hashing
        return hash((self.x, self.y))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __rmul__(self, k):                   # makes 3 * v work, not just v * 3
        return self * k

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __bool__(self):
        return bool(self.x or self.y)

v1, v2 = Vector(3, 4), Vector(1, 2)
print(v1, [v1], repr(v1), str(v1))
print(v1 + v2, v1 * 2, 2 * v1, abs(v1))
print(v1 == Vector(3, 4), v1 != v2, v1 == "x")
print(sorted([v1, v2, Vector(0, 1)]))
print(bool(Vector(0, 0)), bool(v1))
print(len({Vector(1, 1), Vector(1, 1), Vector(2, 2)}))

# Without __hash__, defining __eq__ makes the class unhashable
class P:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x

print(P(1) == P(1))
try:
    {P(1)}
except TypeError as e:
    print("TypeError:", e)

# Container behaviour
class Playlist:
    def __init__(self, *songs):
        self.songs = list(songs)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song in self.songs

pl = Playlist("A", "B", "C")
print(len(pl), pl[0], pl[-1], pl[0:2], "B" in pl, "Z" in pl)
for s in pl:                                 # works because of __getitem__
    print(s, end=" ")
print()