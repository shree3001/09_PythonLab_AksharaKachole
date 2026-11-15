import time
import random

def kth_smallest_pair_sum_naive(arr, k):

    sums = []

    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            sums.append(arr[i] + arr[j])

    sums.sort()
    
    return sums[k - 1]


def count_pairs_less_equal(arr, value):

    n = len(arr)

    count = 0

    j = n - 1

    for i in range(n):

        if i >= j:
            break

        while j > i and arr[i] + arr[j] > value:
            j -= 1

        if j <= i:
            break

        count += j - i

    return count


def kth_smallest_pair_sum_optimized(arr, k):

    # Sort the array
    arr.sort()

    n = len(arr)

    # Smallest possible pair sum
    low = arr[0] + arr[1]

    # Largest possible pair sum
    high = arr[n - 2] + arr[n - 1]

    # Binary search
    while low < high:

        mid = (low + high) // 2

        # Count how many pair sums are <= mid
        count = count_pairs_less_equal(arr, mid)

        if count >= k:
            high = mid
        else:
            low = mid + 1

    return low


# CORRECTNESS TESTS

print("========== CORRECTNESS TESTS ==========")

print("Test 1:",
      kth_smallest_pair_sum_optimized([1, 3, 5, 7], 1))

print("Test 2:",
      kth_smallest_pair_sum_optimized([1, 3, 5, 7], 3))

print("Test 3:",
      kth_smallest_pair_sum_optimized([1, 3, 5, 7], 6))

print("Test 4:",
      kth_smallest_pair_sum_optimized([4, 4, 4], 1))

print("Test 5:",
      kth_smallest_pair_sum_optimized([2, 5, 10], 2))


print("\n========== PERFORMANCE TEST ==========")

random.seed(42)

N = 5000

arr = [random.randint(1, 100000) for _ in range(N)]

K = 1000000

naive_arr = arr.copy()

start = time.time()

naive_answer = kth_smallest_pair_sum_naive(naive_arr, K)

end = time.time()

naive_time = end - start

print("Naive Answer:", naive_answer)
print("Naive Time:", naive_time, "seconds")


optimized_arr = arr.copy()

start = time.time()

optimized_answer = kth_smallest_pair_sum_optimized(
    optimized_arr, K
)

end = time.time()

optimized_time = end - start

print("Optimized Answer:", optimized_answer)
print("Optimized Time:", optimized_time, "seconds")


print("\n========== COMPARISON ==========")

print("Naive Time:", naive_time, "seconds")
print("Optimized Time:", optimized_time, "seconds")

print("\nDifference:",
      naive_time - optimized_time,
      "seconds")
