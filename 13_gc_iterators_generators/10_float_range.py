class FloatRange:
    """Like range(), but for floats, and reusable."""
    def __init__(self, start, stop, step):
        if step == 0:
            raise ValueError("step must not be zero")
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        current = self.start
        while (current < self.stop) if self.step > 0 else (current > self.stop):
            yield round(current, 10)
            current += self.step

    def __len__(self):
        return sum(1 for _ in self)

r = FloatRange(0, 1, 0.25)
print(list(r), list(r), len(r))
print(list(FloatRange(1, 0, -0.5)))
print(sum(FloatRange(0, 1, 0.1)))

try:
    FloatRange(0, 1, 0)
except ValueError as e:
    print("ValueError:", e)