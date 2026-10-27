def validate(record):
    errors = []
    if not record.get("name"):
        errors.append(ValueError("name is required"))
    age = record.get("age")
    if not isinstance(age, int) or age < 0:
        errors.append(ValueError(f"invalid age: {age!r}"))
    if "@" not in record.get("email", ""):
        errors.append(ValueError("invalid email"))
    if errors:
        raise ExceptionGroup("validation failed", errors)     # report every problem at once

for record in ({"name": "Asha", "age": 28, "email": "a@x.com"},
               {"name": "", "age": -1, "email": "x"}):
    try:
        validate(record)
        print("valid:", record)
    except ExceptionGroup as eg:
        print(eg.message, f"({len(eg.exceptions)} problems)")
        for problem in eg.exceptions:
            print("  -", problem)