def typist(s):
    taps = 0
    caps = False
    
    for char in s:
        if char.isupper() and caps == False:
            taps += 1 # turn on caps lock first
            caps = True
        elif char.islower() and caps == True:
            taps += 1 # turn off caps lock first
            caps = False
        taps += 1 # tap actual character
    return taps
"""
John is a typist. He has a habit of typing: he never use the Shift key to switch case, just using only Caps Lock.
Given a string s. Your task is to count how many times the keyboard has been tapped by John.
You can assume that, at the beginning the Caps Lock light is not lit.

For s = "a", the output should be 1.
  John hit button a.

For s = "aa", the output should be 2.
  John hit button a, a.

For s = "A", the output should be 2.
  John hit button Caps Lock, A.

For s = "Aa", the output should be 4.
  John hit button Caps Lock, A, Caps Lock, a.
"""
