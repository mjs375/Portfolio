def even_or_odd(s):
    evens, odds = 0, 0
    for digit in s:
        if not int(digit) % 2: evens += int(digit)
        else: odds += int(digit)
    if evens > odds:
        return "Even is greater than Odd"
    elif odds > evens:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
        
"""
Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.
"""
