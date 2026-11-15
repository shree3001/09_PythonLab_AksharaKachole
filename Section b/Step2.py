# Step 2: Hint 1 
# When checking whether a number x is prime, do you really need to test every divisor up to x minus 1? 
# Ans:No. We only need to check divisors up to √x.
# Write the smallest upper bound you actually need to check up to, and why that is still enough to correctly determine primality.
# Ans:If a number is not prime, it can be written as
# x=a*b
# At least one of these two factors must be less than or equal to √x. So, after checking up to √x, we do not need to check the remaining numbers. 
# Rewrite your program using this smaller bound. 
# Test with N = 2,000,000. Smaller bound version,
import time
import math
N=int(input("Entern:"))
start=time.time()
total=0
for x in range(2,N):
    prime=True
    for d in range(2,int(math.sqrt(x))+1):
     if x%d==0:
      prime=False
      break
    if prime:
     total+=x
print("Sum=",total)
print("Time=",time.time()-start)
#  N = 2,000,000, Time taken: 12.958917617797852
# 4. How much faster was this compared to Step 1? Was it enough, or still slow? 
# This method was faster than the first method because it checks only up to √x instead of checking up to x-1.
# But it can still take some time because every number is still checked separately.