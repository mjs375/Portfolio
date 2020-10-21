def summation(num):
    sum = int()
    for n in range(1, num+1):
        sum += n
    return sum


"""
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
For example:
    summation(2) -> 3
    1 + 2
"""

# # # # # B E T T E R : # # # # # # # 
def summation(num):
    return sum(range(1, num + 1))

# range(1, num+1)
    # range() returns a series of numbers,
    # starting at 1 and stopping at num itself.
# sum() adds the return of range(), which is each number as it counts up
