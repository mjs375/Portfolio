def solution(number):
    fifteen, five, three = int(), int(), int()
    for i in range(1, number): #range is 0 index
        if not i % 15: fifteen += 1 
        elif not i % 5: five += 1
        elif not i % 3: three += 1
    return [three, five, fifteen]


"""
% is MODULUS. It divides (A%B), and yields the remainder as the result.
    if x % i:   =>   if bool(x % i): |OR| if x % i != 0:
Python treats non-zero values as True, 0 as False
    So... 15 % 15 == 0. Thus, False. So, IF (inverse the Boolean) [False>>True]: EXECUTE!
    
    
Write a function that takes an integer and returns an array [A, B, C], where A is the number of multiples of 3 (but not 5) below the given integer, B is the number of multiples of 5 (but not 3) below the given integer and C is the number of multiples of 3 and 5 below the given integer.
    For example, solution(20) should return [5, 2, 1]
"""


