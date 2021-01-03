# Program works in Atom/Python Tutorial, maybe a bug on Codewars?...

def sqInRect(l, w, ans=[]):
    print("Rectangle:",str(l)+"x"+str(w))
    
    #--Start w/ square, return nothing:
    if l == w and ans == []:
        print("...")
        return None
    
    
    #--Find smaller side
    side = min(l, w)
    print("Cut square:",side)
    #
    if side > 0:
        
        if w > l:
            #--
            a = l
            l = w # 'l' is longer again
            w = a # 'w' is longer again
        
        if l > w:
            #--Cut off to make into a square
            l = l - side
            w = w # no change
        
        else: #equal square, last step:
            l = l - side
            w = w - side
        #--Add removed square to list
        ans.append(side)
        print("Remainder:",f"L:{l}", f"W:{w}")
    
    #
    
    if l != 0 and w != 0:
        print("Recurse!", ans, "\n")
        ans = sqInRect(l, w, ans)
    
    print("DONE!:",ans)
    return ans
    
    
    
"""
The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different). Can you translate this drawing into an algorithm?
  You will be given two dimensions
    a positive integer length (parameter named lng)
    a positive integer width (parameter named wdth)
You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.
  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]
"""







"""
The above function works on its own, but not in Codewars because I modified the inputs of the given function, which must have broken the testing apparatus.
"""






def sqInRect(lng, wdth):
    ans=[]
    ans = helper(lng, wdth, ans)
    return ans


def helper(lng, wdth, ans=[]):

    print("Rectangle:",str(lng)+"x"+str(wdth))
    
    #--Start w/ square, return nothing:
    if lng == wdth and ans == []:
        print("...")
        return None
    
    
    #--Find smaller side
    side = min(lng, wdth)
    print("Cut square:",side)
    #
    if side > 0:
        
        if wdth > lng:
            #--
            a = lng
            lng = wdth # 'l' is longer again
            wdth = a # 'w' is longer again
        
        if lng > wdth:
            #--Cut off to make into a square
            lng = lng - side
            wdth = wdth # no change
        
        else: #equal square, last step:
            lng = lng - side
            wdth = wdth - side
        #--Add removed square to list
        ans.append(side)
        print("Remainder:",f"L:{lng}", f"W:{wdth}")
    
    #
    
    if lng != 0 and wdth != 0:
        print("Recurse!", ans, "\n")
        ans = helper(lng, wdth, ans)
    
    print("DONE!:",ans)
    return ans
