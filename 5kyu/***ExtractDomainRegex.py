import re

def domain_name(url): #string
    #match = re.search("h(tt)p",url)
    #print(match.groups())
    match = re.search("https://([A-Za-z_0-9].*)",url)
    print(match.groups())
    
    
""" PYTHON   R E G E X :
.group()    Returns string matched by the RE
.start()    Returns starting position of match
.end()      Returns ending position of match
.span()     Returns a tuple containing (start, end) of match.
    E.g. match.group() => 'string_pattern_searched'

r"..."      r-prefix means the following is a raw string, ie backslash characters are treated literally instead of signifying special treatment
    >'\n'    a single newline
    >r'\n'   2 characters: \  n


"""

""" EXTRACT THE DOMAIN NAME FROM A URL:
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
  domain_name("http://github.com/carbonfive/raygun") == "github" 
  domain_name("http://www.zombie-bites.com") == "zombie-bites"
  domain_name("https://www.cnet.com") == "cnet"
"""
