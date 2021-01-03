def in_array(a1, a2):
    subset = set()
    #--Loop over both lists:
    for word1 in a1:
        for word2 in a2:
            #--If word1 is in/a part of word2:
            if word1 in word2:
                #--Adding to set so no dupes:
                subset.add(word1)
                break
    #--Alphabetize:
    subset = sorted(subset)
    return subset
    
"""
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
  Example 1: 
    a1 = ["arp", "live", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
      returns ["arp", "live", "strong"]
  Example 2: 
    a1 = ["tarp", "mice", "bull"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
      returns []
"""
