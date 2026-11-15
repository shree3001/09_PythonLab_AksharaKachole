# Section C: Problem 2, Count Pairs With a Given Sum 
# Step 1: Naive Version Given a list of N integers and a target sum, count how many pairs of elements, by index, add up exactly to the target (duplicates count separately). Write the naive solution: check every pair against every other pair using two nested loops.
# Test cases (check correctness first): 
# Input: List = [2, 7, 11, 15], Target = 9          Output: 1 
# Input: List = [1, 1, 1], Target = 2                Output: 3 
# Input: List = [3, 3, 4, 4], Target = 7             Output: 4
# Input: List = [5, 5, 5, 5, 5], Target = 10          Output: 10
# Input: List = [1, 2, 3, 4, 5], Target = 100          Output: 0 
# Timing setup (use this exact code so everyone's input list matches): 
# import random random.seed(42) N = 5000       # change to 50000 for the second run 
# arr = [random.randint(1, 20000) for _ in range(N)] 
# target = 20000 

def count_pairs(arr,target):
    count=0
    for i in range(len(arr)):
     for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
         count+=1
    return count    
arr = list(map(int, input("Enter array elements: ").split()))

target = int(input("Enter target: "))

# Function call
answer = count_pairs(arr, target)

print("Number of pairs =", answer)
