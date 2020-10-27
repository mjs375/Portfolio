def find_it(seq):
    dict = {}
    for num in seq: #iterate over list, count occurrences
        if num in dict.keys(): dict[num] = dict.get(num) + 1 #update the dict key (value + 1)
        else: dict[num] = 1 # num is not yet in dict
    for k, v in dict.items(): #iterate over dict
        if v % 2 == 0: pass
        else: odd_num = k
    return odd_num


# dictionary_name[key] = value      #set/update a dict key/value
# dict.get(key) = value             #get a dict value

"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""
