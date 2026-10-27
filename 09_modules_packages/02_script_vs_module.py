import mathutils
import mathutils                   # the second import does NOT run the file again
from mathutils import *            # only is_prime and gcd, because of __all__

print(is_prime(97), gcd(100, 75))
print(__name__, mathutils.__name__)
print(mathutils.__doc__)
print(mathutils.__file__)

try:
    print(PI_ISH)
except NameError as e:
    print("NameError:", e)
print(mathutils.PI_ISH)            # still reachable through the module
print(mathutils._private_helper()) # an underscore is a convention, not a lock