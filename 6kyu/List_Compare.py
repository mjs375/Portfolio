def comp(a1, a2):
    
    # Handle matching/non-matching empties:
    if (a1 == None and a2 == None):
        return True
    if (a1 == [] and a2 == []):
        return True
    if a1 == [] or a1 == None or a2 == [] or a2 == None:
        return False
    # Check lists if (a1**2 == a2)
    check = []
    for num in a1:
        check.append(num**2)
    check.sort()
    a2.sort()

    if check == a2: 
        return True
    else: 
        return False
        
"""
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
"""
