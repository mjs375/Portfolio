def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False

"""
Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.
A few cases:
(-12, 2, -6)  ->  true
(-12, 2, -5)  ->  false
"""
