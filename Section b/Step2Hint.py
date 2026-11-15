# For each number x in the list, the value you actually need to find is target minus x. 
# Instead of scanning the rest of the list to look for it, what data structure lets you check "have I already seen this value" in close to constant time? 
# Rewrite your program using a single pass and this data structure. Test with N = 50,000. 
# Optimized version, N = 50,000, Time taken: 0.005491495132446289
import random
import time

random.seed(42)

N = 50000

arr = [random.randint(1, 20000) for _ in range(N)]

target = 20000


def count_pairs(arr, target):

    seen = set()
    count = 0

    for x in arr:

        required = target - x

        if required in seen:
            count += 1

        seen.add(x)

    return count


start = time.time()

answer = count_pairs(arr, target)

end = time.time()

print("Number of elements (N):", N)
print("Number of pairs:", answer)
print("Time taken:", end - start)
# 8. Compare your naive and optimized times for N = 50,000 side by side. 
# Naive:321.67560029029846
#Optimized:321.67560029029846
# 9. What category of change made this faster? A smarter algorithm, a smarter data structure, or both? Explain. 
# Both a smarter algorithm and a smarter data structure made the program faster. The naive solution checks every possible pair using two nested loops, which takes O(N²) time. 
# The optimized solution uses a single pass through the list and a set to check whether the required value has already been seen. 
# Set lookup takes close to constant time on average, so the overall time is approximately O(N). 
# Therefore, the combination of a smarter algorithm and a smarter data structure makes the optimized solution much faster