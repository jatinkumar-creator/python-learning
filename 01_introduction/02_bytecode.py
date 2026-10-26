import dis

def add(a, b):
    return a * b + 1

print("--- Bytecode of add() ---")
dis.dis(add)

print("\n--- Raw bytecode bytes ---")
print(add.__code__.co_code)

print("\n--- Code object details ---")
print("Argument names :", add.__code__.co_varnames)
print("Constants      :", add.__code__.co_consts)
print("Stack size     :", add.__code__.co_stacksize)