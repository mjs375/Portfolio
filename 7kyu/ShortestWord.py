def find_short(s):
    return min(len(word) for word in s.split(" "))

"""
1. Split() 's' into a list, separated by " " (default is also whitespace).
2. Loop: for word in [new split 's' LIST]
3. [Make a list of] len(word) done in each loop
4. Find the min of that list:
 - the shortest word
"""

# # # # # # # # # # F I R S T _ A T T E M P T : # # # # # # # # # # # # # 

def find_short(s):
    list = s.split(" ") #split 's' into a list, separating by whitespace
    l = "" #shortest word length
    for word in list:
        if l == "":
            l = len(word)
        if len(word) < l:
            l = len(word)
    return l # l: shortest word length

"""
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
"""
