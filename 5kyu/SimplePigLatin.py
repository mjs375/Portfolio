def pig_it(text):
    ans = ""
    words = text.split() #breaks up text by whitespaces
    for w in words:
        if w.isalpha():
            w = w[1:] + w[0:1] + "ay"
            ans = ans + w + " "
        else: #punctuation
            print(w)
            ans = ans  + w + " "
    return ans[:-1] # cut off trailing " "
    
    
    """
    Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
    """
