def triple_x(s):
    for i in range(0, len(s)-2):
        if s[i] == "x":
            if s[i+1] == "x" and s[i+2] == "x":
                return True
            else:
                return False
    else:
        return False

"""
Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".
    tripleX("abraxxxas") → true
    tripleX("xoxotrololololololoxxx") → false
"""
