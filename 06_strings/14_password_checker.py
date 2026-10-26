pwd = input("Password: ")

checks = {
    "length >= 8": len(pwd) >= 8,
    "has upper": any(c.isupper() for c in pwd),
    "has lower": any(c.islower() for c in pwd),
    "has digit": any(c.isdigit() for c in pwd),
    "has symbol": any(not c.isalnum() for c in pwd),
}

for rule, ok in checks.items():
    print(f"{rule:<12} {'OK' if ok else 'MISSING'}")     #Try abc, Password1, and P@ssw0rd!.