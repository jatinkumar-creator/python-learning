import time

def count_primes(limit):
    count = 0
    for n in range(2, limit):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            count += 1
    return count

start = time.perf_counter()
result = count_primes(200_000)
elapsed = time.perf_counter() - start

print(f"Primes below 200000: {result}")
print(f"Time taken: {elapsed:.2f} seconds")