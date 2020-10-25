def sum_of_n(n):
    return [(-1 if n < 0 else 1) * sum(range(i+1)) for i in range(abs(n)+1)]
    # return [...] # a list
    # (-1 if n < 0 else 1)*   # negating sum if n is negative, for negative series
    # sum(range(i+1)    # sum every number between 0-n, inclusive (range 'stops' at 1 before i, hence i+1)
    # for i in range(abs(n)+1)  # now iterate up til 'n' (n+1 is stop), absolute valuing 'n' first

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def sum_of_n(n):
# seq: nth term is sum of numbers 0-n, inclusive.
    ans = []
    if n < 0:
        x = False
    else:
        x = True
    n = abs(n)
    for i in range(0, n+1):
        if x == False:
            temp = sum(range(0, i+1))
            ans.append(temp*-1)
        else:
            ans.append(sum(range(0, i+1)))
    return ans
    
    
"""
    A sequence or a series, in mathematics, is a string of objects, like numbers, that follow a particular pattern. The individual elements in a sequence are called terms. A simple example is 3, 6, 9, 12, 15, 18, 21, ..., where the pattern is: "add 3 to the previous term".
    In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".
    [ 0,  1,    3,      6,   ...]
      0  0+1  0+1+2  0+1+2+3
Your Task:
    Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above. Whenn < 0 return the sequence with negative terms.

"""
