def to_alternating_case(string):
    new = ""
    for char in string:
        
        if char.isupper():
            new += char.lower()
        elif char.islower():
            new += char.upper()
        else:
            new += char
            
    return new

"""
Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:
  "hello WORLD".toAlternatingCase() === "HELLO world"
  "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
"""
