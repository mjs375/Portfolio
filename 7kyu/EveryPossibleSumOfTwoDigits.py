from itertools import combinations
    
def digits(num):
    output = []
    nums = [int(n) for n in str(num)] # convert each digit to an individual integer contained in a list
    pairs = combinations(nums, 2) #make pairwise groupings of all possible combos
    for x, y in pairs:
        output.append(x+y)
    return output

"""
itertools.combinations(iterable, r)
    # what to combine, r[length of tuple] (no repeated elements)
E.g.:
    # combinations('ABCD',2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
"""
