import re
def solution(string,markers):
    print(string)
    print()
    


    string = re.sub("![^>]+$","\n",string,flags=re.MULTILINE)
    print(string)
    print()
    

    string = re.sub("#[^>]+$","",string,flags=re.MULTILINE)
    print(string)
    print()
    
    return string
    
    # re.search(r'\((.*?)\)',s).group(1):
    
"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
    Example:
Given an input string of:
    apples, pears # and bananas
    grapes
    bananas !apples
The output expected would be:
    apples, pears
    grapes
    bananas
"""
