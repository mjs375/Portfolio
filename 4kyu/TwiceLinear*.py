#--Working/EFFICIENT function (*made with various help*):

def dbl_linear(n):
    #--Sequence 'u':
    seq = [1,]
    #--Keep track of which x/y equation is generating the smaller number (to avoid sorting):
    x, y = 0, 0
    for i in range(n):
        #--Calc the latest x/y of seq
        X = 2*seq[x]+1
        Y = 3*seq[y]+1
        #--Now add the smaller number, so that we don't have to sort:
        if X <= Y:
            seq.append(X)
            x += 1
            #--A dupe, don't add to seq:
            if X == Y:
                y += 1
        else:
            seq.append(Y)
            y += 1
    return seq[n]
    



#--Original function, too inefficient:

def dbl_linear(n):
    print("n:",n)
    seq = [1,]
    c=1
    while len(seq) < n+1:
        y = (2*c+1)
        z = (3*c+1)
        if y not in seq:
            seq.append(y)
        if z not in seq:
            seq.append(z)
        c = min(i for i in seq if i > c)
        seq = sorted(seq)
    print("fake:\n",seq)
    pass_in_Y = seq[n]
    go = True
    while go: 
        y = (2*c+1)
        z = (3*c+1)
        if y not in seq:
            seq.append(y)
        if z not in seq:
            seq.append(z)
        seq = sorted(seq)
        if y >= pass_in_Y:
            go = False
        c = min(i for i in seq if i > c)
        
    print("Actual:",seq)
    print("ANS:",seq[n])
    return seq[n]
    
    
    

"""
Consider a sequence u where u is defined as follows:
  The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too. There are no other numbers in u.
  Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
    > 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
  Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

Example:
  dbl_linear(10) should return 22

Note: Focus attention on efficiency
"""
