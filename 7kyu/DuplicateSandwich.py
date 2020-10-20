def duplicate_sandwich(arr): #given a LIST:
    # Ex:
    # # ['dog', 'turtle', 'dove', 'dog', 'cat', 'bird']
    # # # => ['turtle', 'dove']
    length = len(arr)
    for i in range(length): #1st loop: arr[i]:['dog']
        k = i + 1 #offset 2nd loop by 1...
        for j in range(k, length): #2nd loop ... *range(start, stop)
            if arr[i] == arr[j]:
                return arr[i+1:j]
            
            
"""
PYTHON SLICE NOTATION: a[start:stop:step] (start thru stop-1, by step)
a[start:stop]        # items start thru stop-1
a[start:]            # items start thru rest of array
a[:stop]             # items from beginning thru stop-1
a[:]                 # copy of entire array
"""


"""
Task:
In this kata you will be given a list consisting of unique elements except for one thing that appears twice.
Your task is to output a list of everything inbetween both occurrences of this element in the list.
   [0, 1, 2, 3, 4, 5, 6, 1, 7, 8] => [2, 3, 4, 5, 6]
"""
