def student(name, age, city="Delhi", *hobbies, grade="A", **extra):
    print(name, age, city, hobbies, grade, extra)

student("Asha", 20)                                  # positional + defaults
student("Asha", 20, "Pune")                          # positional overrides default
student("Asha", 20, "Pune", "chess", "music")        # extras go to *hobbies
student("Asha", 20, grade="B", phone="123")          # keyword args; extras go to **extra
student(age=20, name="Asha")                         # keyword order doesn't matter
student("Asha", 20, "Pune", "chess", grade="B", x=1)

# Non-default (required) vs default arguments
def power(base, exp=2):                              # base is required, exp is optional
    return base ** exp

print(power(3), power(3, 3), power(exp=3, base=2))

# Arbitrary positional arguments
def total(*args):
    print(type(args), args)
    return sum(args)

print(total(), total(1), total(1, 2, 3))

# Arbitrary keyword arguments
def show(**kwargs):
    print(type(kwargs), kwargs)
    for k, v in kwargs.items():
        print(f"  {k} = {v}")

show(name="Asha", age=28)

# Unpacking at the call site
nums = [1, 2, 3]
info = {"name": "Asha", "age": 28}
print(total(*nums))
show(**info)

# Wrong calls
calls = [
    lambda: power(),                     # missing required argument
    lambda: power(1, 2, 3),              # too many arguments
    lambda: power(2, base=3),            # same argument twice
    lambda: power(2, wrong=3),           # unknown keyword
]
for call in calls:
    try:
        call()
    except TypeError as e:
        print("TypeError:", e)