import re
def increment_string(s):
    print("String:", s)
    num = re.search("[0-9]*$", s) # find numbers on end
    num = num.group() # stringify
    orig = num
    
    if num == "": # No number ending string
        print("no num")
        return s + "1"
    
    l = len(re.search("^0*", num).group()) # count leading zeros
    substring = re.sub(num, "", s) # obtain string w/o numbers
    num = num.lstrip("0") #remove leading zeroes
    print(l, "|", num)
    if num: # if a trailing number, increment by 1
        num = int(num) +1
        print("New:", num)
    else: # no num, add '1' to end (but also plus any leading zeros back)
        num = 1
        
    if False:
        pass
    else: # Add new number (& leading zeroes) back to substring
        substring += "0"*l + str(num)
    return substring

    
"""
.group() :returns the match in the string
"""
