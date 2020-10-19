import array as arr

def arr(n=None): #default 'n' is empty, in case not provided 
    # [ the numbers 0 to N-1 ]
    array = []
    if n == None: #if 'n' isn't provided:
        return array
    else:
        for i in range(n): #range(0 to n-1)
            array.append(i)
        return array

    
    
"""
We want an array, but not just any old array, an array with contents!
Write a function that produces an array with the numbers 0 to N-1 in it.
For example, the following code will result in an array containing the numbers 0 to 4:
arr(5) // => [0,1,2,3,4]
"""
