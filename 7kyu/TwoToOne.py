# COMBINE, ALPHABETIZE, UNIQUE-IZE:
def longest(s1, s2):
    word = sorted(s1+s2) #concatenate & alphabetize the strings into a list
    output = "" #for output
    for a in word: #for element in list
        for b in word: # for element2 in list
            if a == b and a not in output: #don't add dupes
                output += a
    return output
    
"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters, each taken only once - coming from s1 or s2.
"""
    
    
# # GENIUS SOLUTION: ##
# return "".join(sorted(set(a1+a2)))
# # Return an empty string, to which is joined, a sorted/alphabetized set (unique values only) of a1+a2
