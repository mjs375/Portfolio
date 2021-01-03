def create_array_of_tiers(n):
    n = str(n)
    return [ n[0:i+1] for i,v in enumerate(n) ]

"""
Create a function that takes a number and returns an array of strings containing the number cut off at each digit.

Examples
420 should return ["4", "42", "420"]
2017 should return ["2", "20", "201", "2017"]
"""
