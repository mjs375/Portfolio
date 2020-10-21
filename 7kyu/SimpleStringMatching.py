import re #imports the RegEx module
def solve(a,b):
      
    if "*" in a: #insert regex
        a = a.replace("*",".*")
    a = "^" + a + "$"
    # "^" fixes to start of string
    # "$" fixes to end of string
    # "." can be any 1 character
    # "*" means previous (".") can be any num of occurrences (incl. 0)
    y = re.search(a,b)

    if y:
        return True
    else:
        return False

# # # # # N O T _ MY _ C O D E _ B U T _ S I M P L E R _ V E R S I O N _ O F _ M I N E : # # # # # 

import re

def solve(a, b):
    return bool(re.match(f"^{a.replace('*', '.*')}$", b))
"""
*: zero of more occurrences (of what precedes)
.: any single character
^/$: starts with/ends with...
f-string "...": allows Python functions inside the {...}
re.match(a, b): searches just the first line of the string. Returns first match-instance of substring[a] within the string[b].
Bool(): converts a value to True/False (essentially if False/None/empty, returns False)
"""
