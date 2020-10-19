def get_middle(s):
    # "//" is 'floor division', which basically cuts off the decimal point remainer (4.5 becomes 4.0)
    if len(s) % 2 != 0: #odd: middle character
            # len(s)=11
        mid = s[len(s)//2] #s[11//2] = 5.5 = s[5]
        return mid
    else: #even: get middle 2 characters #s=10
            #len(s)=10
        L = s[(len(s) // 2) - 1] #s[(10//2)-1] = 5-1 = s[4]
        R = s[len(s) // 2] #s[10//2] = s[5]
        return L + R
    
    
"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
- Examples:
    Kata.getMiddle("test") should return "es"
    Kata.getMiddle("testing") should return "t"
"""
