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
