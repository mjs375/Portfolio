def swap_vowel_case(st): 
    vowels = "aeiouAEIOU"
    dupe = ""
    for c in st:
        if c in vowels:
            if c.isupper():
                dupe += c.lower()
            elif c.islower():
                dupe += c.upper()
        else:
            dupe += c
    return dupe

  
"""
Challenge:

Given a string, return a copy of the string with the vowels' case swapped.

For this kata, assume that vowels are in the set "aeouiAEOUI".

Example: Given a string "C is alive!", your function should return "C Is AlIvE!"
"""
