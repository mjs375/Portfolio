def even_last(numbers): 
    if numbers == []: return 0
    print(numbers)
    ans = int() # ans = 0
    for num in range(0, len(numbers), 2):
        print(numbers[num])
        ans += numbers[num]
    ans *= numbers[-1] # multiply by last num in numbers
    return ans
  
"""
Given a sequence of integers, return the sum of all the integers that have an even index, multiplied by the integer at the last index.
  Indices in sequence start from 0.
  If the sequence is empty, you should return 0.
"""
