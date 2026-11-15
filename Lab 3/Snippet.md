Snippet 1



def find\_max(arr):

&#x20;   max\_val = arr\[0]

&#x20;   for i in range(1, len(arr)):

&#x20;       if arr\[i] > max\_val:

&#x20;           max\_val = arr\[i]

&#x20;   return max\_val



Time complexity: O(n) 

Space complexity: O(1) 

Justify: The loop checks every element once, while only one extra variable max\_val is used.





Snippet 2



def has\_duplicate(arr):

&#x20;   for i in range(len(arr)):

&#x20;       for j in range(i + 1, len(arr)):

&#x20;           if arr\[i] == arr\[j]:

&#x20;               return True

&#x20;   return False



Time complexity:  O(n²)

Space complexity: O(1)

Justify: Two nested loops compare pairs of elements, giving approximately n × n comparisons.





Snippet 3



def sum\_digits(n):

&#x20;   if n == 0:

&#x20;       return 0

&#x20;   return n % 10 + sum\_digits(n // 10)



Time complexity: O(log n)

Space complexity: O(log n)

Justify: Each recursive call removes one digit by doing n // 10, so there are about log₁₀(n) calls.





Snippet 4



def print\_pairs(arr):

&#x20;   n = len(arr)

&#x20;   result = \[]

&#x20;   for i in range(n):

&#x20;       for j in range(n):

&#x20;           result.append((arr\[i], arr\[j]))

&#x20;   return result



Time complexity: O(n²)

Space complexity: O(n²)

Justify: Two nested loops generate n² pairs and store all of them in result.





Snippet 5



def binary\_search(arr, target):

&#x20;   low, high = 0, len(arr) - 1

&#x20;   while low <= high:

&#x20;       mid = (low + high) // 2

&#x20;       if arr\[mid] == target:

&#x20;           return mid

&#x20;       elif arr\[mid] < target:

&#x20;           low = mid + 1

&#x20;       else:

&#x20;           high = mid - 1

&#x20;   return -1



Time complexity: O(log n)

Space complexity: O(1)

Justify: The search range is divided approximately in half during every iteration, using only a few variables.





Snippet 6



def matrix\_multiply(a, b):

&#x20;   n = len(a)

&#x20;   result = \[\[0] \* n for \_ in range(n)]

&#x20;   for i in range(n):

&#x20;       for j in range(n):

&#x20;           for k in range(n):

&#x20;               result\[i]\[j] += a\[i]\[k] \* b\[k]\[j]

&#x20;   return result





Time complexity: O(n³)

Space complexity: O(n²)

Justify: Three nested loops perform n³ operations, while the result matrix requires n² space.





Snippet 7



def to\_sparse(matrix):

&#x20;   triples = \[]

&#x20;   for r in range(len(matrix)):

&#x20;       for c in range(len(matrix\[0])):

&#x20;           if matrix\[r]\[c] != 0:

&#x20;               triples.append((r, c, matrix\[r]\[c]))

&#x20;   return triples



Time complexity (in terms of matrix dimensions m and n): O(mn)

Space complexity (in terms of k non-zero elements): O(k)

Justify: Every one of the m × n matrix elements is checked, and only the k non-zero elements are stored.





Snippet 8



def process(arr):

&#x20;   n = len(arr)

&#x20;   for i in range(n):

&#x20;       print(arr\[i])

&#x20;   for j in range(n):

&#x20;       for k in range(n):

&#x20;           print(arr\[j], arr\[k])



Time complexity: O(n³)

Justify: The outer loop is O(n), and inside it are two nested O(n) loops, giving n × n × n = n³.





Snippet 9



def check\_first\_ten(arr):

&#x20;   for i in range(len(arr)):

&#x20;       for j in range(10):

&#x20;           if arr\[i] == j:

&#x20;               return True

&#x20;   return False



Time complexity: O(n)

Justify: For every array element, the inner loop always runs only 10 times, so 10n = O(n).





Snippet 10



def reverse\_new(arr):

&#x20;   reversed\_arr = \[]

&#x20;   for i in range(len(arr) - 1, -1, -1):

&#x20;       reversed\_arr.append(arr\[i])

&#x20;   return reversed\_arr



Time complexity: O(n) 

Space complexity: O(n)

Justify: Every element is visited once and a new array containing all n elements is created.





Snippet 11



def reverse\_in\_place(arr):

&#x20;   left, right = 0, len(arr) - 1

&#x20;   while left < right:

&#x20;       arr\[left], arr\[right] = arr\[right], arr\[left]

&#x20;       left += 1

&#x20;       right -= 1

&#x20;   return arr



Time complexity: O(n)

Space complexity: O(1)

Justify: The elements are swapped about n/2 times, and no extra array is created.





Snippet 12



def factorial(n):

&#x20;   if n == 0 or n == 1:

&#x20;       return 1

&#x20;   return n \* factorial(n - 1)



Time complexity: O(n)

Space complexity: O(n)

Justify: The function makes n recursive calls, and each call remains on the recursion stack.





Snippet 13



def fibonacci(n):

&#x20;   if n <= 1:

&#x20;       return n

&#x20;   return fibonacci(n - 1) + fibonacci(n - 2)



Time complexity: O(2ⁿ)

Space complexity: O(n)

Justify: Each call recursively creates two more calls, producing exponential time, while the maximum recursion depth is n.





Snippet 14



def count\_pairs\_with\_sum(arr, target):

&#x20;   seen = set()

&#x20;   count = 0

&#x20;   for num in arr:

&#x20;       if target - num in seen:

&#x20;           count += 1

&#x20;       seen.add(num)

&#x20;   return count



Time complexity: O(n) average

Space complexity: O(n)

Justify: The array is traversed once and set lookup/insertion takes O(1) average time, while the set can store up to n elements.





Snippet 15



def print\_all\_subsets(arr):

&#x20;   n = len(arr)

&#x20;   for i in range(2 \*\* n):

&#x20;       subset = \[]

&#x20;       for j in range(n):

&#x20;           if i \& (1 << j):

&#x20;               subset.append(arr\[j])

&#x20;       print(subset)



Time complexity: O(n × 2ⁿ)

Justify: There are 2ⁿ subsets and each subset requires up to n checks to construct.





Snippet 16



def merge\_sorted(a, b):

&#x20;   result = \[]

&#x20;   i = j = 0

&#x20;   while i < len(a) and j < len(b):

&#x20;       if a\[i] <= b\[j]:

&#x20;           result.append(a\[i])

&#x20;           i += 1

&#x20;       else:

&#x20;           result.append(b\[j])

&#x20;           j += 1

&#x20;   result.extend(a\[i:])

&#x20;   result.extend(b\[j:])

&#x20;   return result



Time complexity: O(n + m)

Space complexity: O(n + m)

Justify: Each element of arrays a and b is processed once and copied into the new result array.





Snippet 17



def is\_palindrome(s):

&#x20;   return s == s\[::-1]



Time complexity: O(n)

Space complexity: O(n)

Justify: Slicing s\[::-1] creates a reversed copy of the string and comparison takes linear time.





Snippet 18



def flatten(matrix):

&#x20;   flat = \[]

&#x20;   for row in matrix:

&#x20;       for val in row:

&#x20;           flat.append(val)

&#x20;   return flat



Time complexity (in terms of m rows and n columns): O(mn)

Space complexity: O(mn)

Justify: All m × n elements are visited and stored in the new flat list.





Snippet 19



def power(base, exp):

&#x20;   if exp == 0:

&#x20;       return 1

&#x20;   return base \* power(base, exp - 1)



Time complexity: O(exp)

Space complexity: O(exp)

Justify: The exponent decreases by 1 in every recursive call, resulting in exp calls and recursion depth.



Snippet 20



def fast\_power(base, exp):

&#x20;   if exp == 0:

&#x20;       return 1

&#x20;   half = fast\_power(base, exp // 2)

&#x20;   if exp % 2 == 0:

&#x20;       return half \* half

&#x20;   return half \* half \* base



Time complexity: O(log exp)

Space complexity: O(log exp)

Justify: The exponent is divided by 2 in every recursive call, so both the number of calls and recursion depth are logarithmic.



Snippet 21



def has\_common\_element(a, b):

&#x20;   for x in a:

&#x20;       for y in b:

&#x20;           if x == y:

&#x20;               return True

&#x20;   return False



Time complexity (in terms of the sizes of a and b): O(nm)

Space complexity: O(1)

Justify: Every element of a may be compared with every element of b, requiring n × m comparisons.





Snippet 22



def build\_frequency\_map(arr):

&#x20;   freq = {}

&#x20;   for val in arr:

&#x20;       freq\[val] = freq.get(val, 0) + 1

&#x20;   return freq



Time complexity: O(n) average

Space complexity: O(n)

Justify: The array is traversed once and dictionary operations take O(1) average time, with up to n distinct keys stored.

