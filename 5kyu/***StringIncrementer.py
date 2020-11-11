import re
def increment_string(s):
    num = re.search("[0-9]*$", s) # find numbers on end
    num = num.group() # now a string
    l = len(num) # account for to add back in leading zeroes
    num = num.lstrip("0") #remove leading zeroes
    
"""
.group() :returns the match in the string
"""
