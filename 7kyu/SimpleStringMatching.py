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
