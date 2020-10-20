def two_oldest_ages(ages):
    a, b = 0, 0
    a = max(ages)
    ages.remove(a)
    b = max(ages)
    list = []
    list.append(b)
    list.append(a)
    return list

"""
The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].
The order of the numbers passed in could be any order. The array will always include at least 2 items.
For example:
    two_oldest_ages([1, 3, 10, 0]) # should return [3, 10]
"""

# # # # # # # # # # B E S T _ P R A C T I C E : # # # # # # # # # # # # # #
def two_oldest_ages(ages):
    return sorted(ages)[-2:]
    #Python slice notation:
        # '-2:' means start 2 from the end (thus the two oldest), to the end. Brilliant!
