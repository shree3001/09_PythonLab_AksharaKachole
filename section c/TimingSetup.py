import time
import random

random.seed(42)

# N = 5000
N=50000

arr = [random.randint(1, 20000) for _ in range(N)]

target = 20000

start = time.time()

count = 0

for i in range(len(arr)):

    for j in range(i + 1, len(arr)):

        if arr[i] + arr[j] == target:
            count += 1

print("Count =", count)

print("Time taken:", time.time() - start)
# Naive version, N = 5,000, Time taken:  1.455493688583374
# Naive version, N = 50,000, Time taken:321.67560029029846
#  7. What happened to the time when N grew by 10 times? Does this match what you would expect from a nested loop approach? 
# When N increased from 5,000 to 50,000, the execution time increased significantly. This is because the solution uses two nested loops, so the number of comparisons grows approximately as N^2.

# When N becomes 10 times larger, the amount of work becomes roughly:

#  10^2 = 100 

# times larger.

# Therefore, the large increase in execution time is expected for a nested-loop approach. This shows that the naive solution has O(N²) time complexity.