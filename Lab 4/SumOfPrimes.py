
import time

def sum_of_primes_sieve(N):
    if N <= 2:
        return 0

    is_prime = [True] * N
    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while p * p < N:
        if is_prime[p]:
            for i in range(p * p, N, p):
                is_prime[i] = False
        p += 1

    total = 0

    for num in range(2, N):
        if is_prime[num]:
            total += num

    return total


# Correctness testing
print("N = 10:", sum_of_primes_sieve(10))
print("N = 2:", sum_of_primes_sieve(2))
print("N = 3:", sum_of_primes_sieve(3))
print("N = 20:", sum_of_primes_sieve(20))
print("N = 100:", sum_of_primes_sieve(100))


# Time measurement
N = 2000000

start = time.time()
result = sum_of_primes_sieve(N)
end = time.time()

print("N =", N)
print("Sum:", result)
print("Time taken:", end - start)