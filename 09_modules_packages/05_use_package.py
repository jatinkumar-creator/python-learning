import toolkit
from toolkit import slugify, is_prime
from toolkit.data import stats
from toolkit.data.stats import mean
import toolkit.numutils as nu

print(toolkit.__version__)
print(slugify("Hello, World! It's Python"))
print(is_prime(97), nu.factorial(6))
print(mean([1, 2, 3, 4]), stats.median([5, 1, 3]))
print(stats.word_counts("the cat and the hat").most_common(1))

print(toolkit.__file__)
print(toolkit.__path__)
print(toolkit.__name__, stats.__name__)
print([n for n in dir(toolkit) if not n.startswith("_")])

try:
    mean([])
except ValueError as e:
    print("ValueError:", e)