name = input("Enter your name: ")
print("Hello,", name)

age = input("Enter age: ")
print(type(age))                       # always str

a, b = map(int, input("Two numbers: ").split())
print(a + b)

nums = list(map(int, input("Numbers separated by spaces: ").split()))
print(nums, sum(nums))