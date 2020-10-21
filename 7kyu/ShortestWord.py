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
