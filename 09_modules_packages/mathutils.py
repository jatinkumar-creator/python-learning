"""Small math helpers."""
print("mathutils is being loaded, __name__ =", __name__)

__all__ = ["is_prime", "gcd"]      # controls what "from mathutils import *" exposes

PI_ISH = 3.14

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def _private_helper():
    return "internal use only"

if __name__ == "__main__":
    print("Running mathutils directly")
    print(is_prime(29), gcd(48, 18))