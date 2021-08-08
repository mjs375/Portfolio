def check_password(pw):
    print(pw)
    
    if len(pw) > 20 or len(pw) < 8:
        return "not valid"
    
    u, l, d, s = 0,0,0,0
    no = 0
    
    for c in pw:
        if c.islower(): l += 1
        elif c.isupper(): u += 1
        elif c.isdigit(): d += 1
        elif c in "!@#$%^&*?": s += 1
        else: no += 1
    
    if u > 0 and l > 0 and d > 0 and s > 0 and no == 0:
        return "valid"
    else: return "not valid"
        
"""
Your users' passwords were all stolen in the Yahoo! hack, and it turns out they have been lax in creating secure passwords. Create a function that checks their new password (passed as a string) to make sure it meets the following requirements:
  - Between 8 - 20 characters
  - Contains only the following characters (and at least one character from each category):
    - uppercase letters,
    - lowercase letters,
    - digits,
    - special characters from !@#$%^&*?
Return "valid" if passed or "not valid" otherwise.
"""
