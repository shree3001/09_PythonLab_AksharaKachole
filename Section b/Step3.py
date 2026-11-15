# Step 3: Hint 2 — Sieve of Eratosthenes
# Answer:
# The sieve finds all prime numbers together. First, we consider the numbers as prime. Then we start from 2 and mark its multiples as not prime.
#  We repeat this for the next unmarked number. At the end, the numbers which are not marked are prime.
import time
start=time.time()
n=int(input("enter n:"))
is_prime=[True]*n
is_prime[0]=False
is_prime[1]=False
p=2
while p*p<n:
  if is_prime[p]:
    for multiple in range(p*p,n,p):
     is_prime[multiple]=False
  p+=1
total=0
for i in range(2,n):
 if is_prime[i]:
   total+=i
print("Sum:",total)
print("Time taken:",time.time()-start)   
#  N = 2,000,000
# Time taken:14.929934024810791
# 5. Compare all three times for N = 2,000,000 side by side. 
# Naive:             
# Smaller bound:      12.958917617797852 
# Sieve:               14.929934024810791
# 6. Which single change gave the biggest jump in speed? Explain why. 
# 6. Which single change gave the biggest jump in speed?
# Answer:

# The Sieve of Eratosthenes gave the biggest improvement.

# The naive and smaller-bound methods test each number separately. 
# The sieve instead finds all prime numbers together and avoids repeatedly solving the same primality problem.