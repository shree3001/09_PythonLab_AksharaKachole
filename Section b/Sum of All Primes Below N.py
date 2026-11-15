# Section B: Problem 1, Sum of All Primes Below N
# Step 1: Naive Version 
# Q:Write a program that computes the sum of all prime numbers strictly below N, checking every number from 2 up to N minus 1, and for each one, testing all possible divisors to decide if it is prime. 
import time
N=2000000
start=time.time()
total=0
for x in range(2,N):
    prime=True
    for d in range(2,x):
     if x%d==0:
      prime=False
      break
    if prime:
     total+=x
print("Sum=",total)
print("Time=",time.time()-start)
# Timing

# Naive version, N = 50,000, Time taken: 6.368677616119385


# Naive version, N = 2,000,000, Time taken:

# 3. What did you observe?Did the time grow the way you expected when N grew by about 40 times? 
# Answer:
# When N became bigger, the program took much more time. This was expected because the program checks many divisors for every number.
#  So, increasing N makes the number of calculations increase very quickly.
