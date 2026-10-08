# Section D: Problem 3, K-th Smallest Pairwise Sum  
# Given a list of N integers and an integer K, find the K-th smallest value among all possible pairwise sums (choosing two different indices, order does not matter).
# Read N, then K, then the N integers. Test cases (check correctness first):
# Input: List = [1, 3, 5, 7], K = 1          Output: 4 
# Input: List = [1, 3, 5, 7], K = 3          Output: 8 
# Input: List = [1, 3, 5, 7], K = 6          Output: 12 
# Input: List = [4, 4, 4], K = 1              Output: 8 
# Input: List = [2, 5, 10], K = 2             Output: 12
# Step 1: Naive Version Generate every pairwise sum, store them, sort, pick the K-th one.
# Note why this becomes slow and memory heavy as N grows (think about how many pairs exist for N = 5000). 
# Timing setup: import random random.seed(42) N = 5000 arr = [random.randint(1, 100000) for _ in range(N)] K = 1000000
# Naive version, N = 5,000, Time taken: 5.45027494430542
import time
import random


# STEP 1: NAIVE VERSION

def kth_smallest_pair_sum_naive(arr, k):

    sums = []

    n = len(arr)

    # Generate all possible pairwise sums
    for i in range(n):
        for j in range(i + 1, n):
            sums.append(arr[i] + arr[j])

    # Sort all sums
    sums.sort()

    # K-th smallest element
    return sums[k - 1]


# STEP 2 & 3: OPTIMIZED COUNTING FUNCTION

def count_pairs_less_equal(arr, value):

    n = len(arr)

    count = 0

    # Right pointer
    j = n - 1

    for i in range(n):

        if i >= j:
            break

        # Move j until the sum becomes <= value
        while j > i and arr[i] + arr[j] > value:
            j -= 1

        if j <= i:
            break

        # All positions from i+1 to j are valid
        count += j - i

    return count


# STEP 4: OPTIMIZED VERSION
# Binary Search on the Answer

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


# PERFORMANCE TEST
# N = 5000
# K = 1000000

print("\n========== PERFORMANCE TEST ==========")

random.seed(42)

N = 5000

arr = [random.randint(1, 100000) for _ in range(N)]

K = 1000000


# NAIVE TIMING


naive_arr = arr.copy()

start = time.time()

naive_answer = kth_smallest_pair_sum_naive(naive_arr, K)

end = time.time()

naive_time = end - start

print("Naive Answer:", naive_answer)
print("Naive Time:", naive_time, "seconds")


# ------------------------------------------------------------
# OPTIMIZED TIMING
# ------------------------------------------------------------

optimized_arr = arr.copy()

start = time.time()

optimized_answer = kth_smallest_pair_sum_optimized(
    optimized_arr, K
)

end = time.time()

optimized_time = end - start

print("Optimized Answer:", optimized_answer)
print("Optimized Time:", optimized_time, "seconds")


# ============================================================
# FINAL COMPARISON
# ============================================================

print("\n========== COMPARISON ==========")

print("Naive Time:", naive_time, "seconds")
print("Optimized Time:", optimized_time, "seconds")

print("\nDifference:",
      naive_time - optimized_time,
      "seconds")


# Pehle 5 correctness tests:


#  CORRECTNESS TESTS 
# Test 1: 4
# Test 2: 8
# Test 3: 12
# Test 4: 8
# Test 5: 12
# Phir `N = 5000` ka timing:

#  PERFORMANCE TEST
# Naive Answer: ...
# Naive Time: ... seconds

# Optimized Answer: ...
# Optimized Time: ... seconds


