import random

secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess (1-10): "))
    attempts += 1
    if guess == secret:
        print(f"Correct! You took {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")