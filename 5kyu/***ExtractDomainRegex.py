import re

def domain_name(url): #string
    print(url)
    #match = re.search("h(tt)p",url)
    #print(match.groups())
    match = re.search("(?:http://www.|http://|www.|https://|^)([A-Za-z0-9-]*)(?:\.)",url) #EXPLANATION BELOW
    print(match.group(0))
    #print(match.group(1))
    #print(match.group(2))
    return match.group(1)

#Explanation of Regex(^):
    # (?:  )   # a way to group, a 'non'-capture group/version: turns off its 'capturedness'
    # http|www|...  # a set of substrings to search for, separated by the | which means 'or'
    # ^     # the last |^ in the noncapture group means, just start at the beginning of the entire text (for websites with no preceding www.)
    # ([A-Za-z0-9-]*)   #the content we actually want: a group of alpha-numeric-dash letters (*any amount)
    #(\.)   #the \ 'escapes' the period, so it is an actual period, not interpreted as a regex expression
    
    
""" PYTHON   R E G E X :
.group()    Returns string matched by the RE. Use capture groups (...) in the regex.
    >> result.group(1) will return 1st capture group, ie stuff within (...)
    >> result.group(0) will return the entire_matched_text
.groups()
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
