
import time
import random


# Naive Approach
#def count_pairs_naive(arr, target):
#    count = 0
#    n = len(arr)

 #   for i in range(n):
 #       for j in range(i + 1, n):
 #           if arr[i] + arr[j] == target:
 #               count += 1

 #   return count


# Optimized Approach
def count_pairs_optimized(arr, target):
    seen = {}
    count = 0

    for num in arr:
        complement = target - num

        if complement in seen:
            count += seen[complement]

        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    return count


# Correctness Testing
print("Naive Approach:")
print(count_pairs_naive([2, 7, 11, 15], 9))
print(count_pairs_naive([1, 1, 1], 2))
print(count_pairs_naive([3, 3, 4, 4], 7))
print(count_pairs_naive([5, 5, 5, 5, 5], 10))
print(count_pairs_naive([1, 2, 3, 4, 5], 100))


# Generate random data
random.seed(42)

N = 5000
arr = [random.randint(1, 20000) for _ in range(N)]
target = 20000

# Naive timing for N = 5000
start = time.time()
result = count_pairs_naive(arr, target)
end = time.time()

print("Naive N = 5000:", end - start)


# Naive timing for N = 50000
N = 50000
arr = [random.randint(1, 20000) for _ in range(N)]

start = time.time()
result = count_pairs_naive(arr, target)
end = time.time()

print("Naive N = 50000:", end - start)


# Optimized timing for N = 50000
start = time.time()
result = count_pairs_optimized(arr, target)
end = time.time()

print("Optimized N = 50000:", end - start)
print("Total pairs:", result)