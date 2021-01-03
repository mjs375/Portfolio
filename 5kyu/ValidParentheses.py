def valid_parentheses(string):
    hill = 0
    
    for char in string:
        #--if a letter, just ignore
        if char == "(" or char == ")":
            if char == "(":
                hill += 1
            if char == ")":
                hill -= 1
                if hill < 0: # you've closed too many!
                    return False
    if hill == 0: # you finished closing all the last ")"
        return True
    else: # you have some unmatched, final ")"
        return False
"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
  Examples
    "()"              =>  true
    ")(()))"          =>  false
    "("               =>  false
    "(())((()())())"  =>  true
"""
