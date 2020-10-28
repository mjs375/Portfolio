def move_zeros(array): #list
    indexes = []
    for index, i in enumerate(array): # GET INDEXES OF ZERO
        if type(i) == int or type(i) == float:
            if i == 0 or i == 0.0:
                indexes.append(index)
    x = len(indexes)
    
    newarray = []    
    for index, value in enumerate(array):
        if index in indexes:
            pass
        else:
            newarray.append(value)
            
    for times in range(x):
        newarray.append(0)

    return newarray
    
    
"""
PROBLEM: The real difficulty with the problem is that, in Python, 0 == False, so the first attempt deleted Falses as well... needed to go back and check if type int/float (or NOT type bool...)
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
  move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
"""
