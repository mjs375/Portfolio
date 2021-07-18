def duplicate_encode(word):
    word = word.lower()
    # Count dupes
    tally = {}
    for char in word:
        if char in tally:
            tally[char] += 1
        else:
            tally[char] = 1
    # Create new word
    new = ""
    for char in word:
        if tally[char] == 1:
            new += "("
        else:
            new += ")"
    return new
            
"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""
