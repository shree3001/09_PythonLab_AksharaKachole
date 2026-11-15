# Python Lab 4 - Algorithm Optimization and Time Complexity

## Section A: Before You Start

1. Code runs faster when it uses an efficient algorithm and avoids unnecessary operations.
2. Functions help avoid repeating the same code.

## Problem 1: Sum of All Primes Below N

Implemented three approaches:

- Naive Approach
- Square Root Optimization
- Sieve of Eratosthenes

### Recorded Results

| Approach              |   Input N |      Time |
| --------------------- | --------: | --------: |
| Naive                 |    50,000 | 5.726 sec |
| Square Root           |    50,000 | 0.057 sec |
| Sieve of Eratosthenes | 2,000,000 | 0.376 sec |

The Sieve of Eratosthenes was efficient because it marks multiples of prime numbers instead of checking every number individually.

## Problem 2: Count Pairs With Given Sum

Implemented:

- Naive Approach using nested loops
- Optimized Approach using a dictionary

The optimized approach reduces repeated searching by storing previously seen numbers.

## Problem 3: K-th Smallest Pairwise Sum

Implemented:

- Naive Approach using pair generation and sorting
- Optimized Approach using sorting, binary search and two pointers

### Recorded Results

| Approach  |       Time |
| --------- | ---------: |
| Naive     | 10.890 sec |
| Optimized |  0.012 sec |

Both approaches produced the same answers for all correctness test cases.

## Section E: Reflection

1. Efficient algorithms and data structures reduce execution time.
2. Avoiding unnecessary repeated work makes programs faster.
3. My favourite technique is using dictionaries for faster searching and counting.
