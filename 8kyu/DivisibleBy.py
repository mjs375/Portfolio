def is_divisible(n,x,y):
    return True if not n % x and not n % y else False
    
# True if not n % x
    # n % x: Python treats nums as True, and 0 as False
    # if n%x == 0 (False),
    # the 'not' inverts False to True


"""
Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
"""
