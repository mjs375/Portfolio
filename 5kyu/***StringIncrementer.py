import re
def increment_string(s):
    print("String:", s)
    num = re.search("[0-9]*$", s) # find numbers on end
    num = num.group() # now a string
    l = len(re.search("^0*", num).group()) # count leading zeros
    num = num.lstrip("0") #remove leading zeroes
    print(l, "|", num)
    if num:
        num = int(num) +1
        print("New:", num)
    else: # no num, add '1' to end (but also plus any leading zeros back)

"""
.group() :returns the match in the string
"""
