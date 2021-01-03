import math
def next_perfect_square(n):
    print(n)
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    root = math.sqrt(n)
    
    if root.is_integer():
        root += 1
    else:
        root = math.ceil(root)
    
    nextperfect = root*root
    return nextperfect
"""
Write a function name nextPerfectSquare / next_perfect_square that returns the first perfect square that is greater than its integer argument. A perfect square is a integer that is equal to some integer squared. For example 16 is a perfect square because 16=4*4.
  Example:
 (n   next perfect square)
  6    9
  36   49 
  0    1
  -5   0 
  
Caution! the largest number tested is close to Number.MAX_SAFE_INTEGER
"""
