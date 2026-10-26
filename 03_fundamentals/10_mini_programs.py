# 1. Simple interest
principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
years = int(input("Years: "))
interest = principal * rate * years / 100
print(f"Interest: {interest:.2f}")
print(f"Total: {principal + interest:.2f}")

# 2. Celsius to Fahrenheit
c = float(input("Celsius: "))
print(f"{c}°C = {c * 9 / 5 + 32:.1f}°F")

# 3. Seconds to HH:MM:SS
total = int(input("Seconds: "))
h = total // 3600
m = (total % 3600) // 60
s = total % 60
print(f"{h:02d}:{m:02d}:{s:02d}")

# 4. Sum of digits using // and %
n = int(input("Number: "))
digit_sum = 0
while n > 0:
    digit_sum += n % 10
    n //= 10
print(digit_sum)