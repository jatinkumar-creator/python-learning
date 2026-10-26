import importlib
helper = importlib.import_module("09_helper")   # a file name starting with a digit can't be imported with a plain `import`
print(helper.greet("Jatin"))