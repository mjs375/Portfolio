import re
def solve_runes(runes):
    numlist = re.split('[+\-*/=]',runes) #Split string into nums/signs
    #
    for i, elem in enumerate(numlist): #Replace "" with a negative sign "-":
        try:
            if numlist[i-1] == "":
                numlist[i] = '-' + numlist[i]
        except: pass
    #
    nums = [num for num in numlist if num != ""] # Then remove spaces from list
    #
    num1, num2, result = nums[0], nums[1], nums[2]
    match = re.search('[+\-*/=]',runes[1:]) #Exclude [0] of equation: can't be the operation, but can be a negative sign
    op = match[0] # the operation matched
    #
    equation = f"{num1}{op}{num2}" # ('?' still inside)
    #
    for i in range(10): # Loop, replace '?' w/0-9'.
        L = re.sub(r"\?", str(i), equation) #OR# x = equation.replace("?",str(i))        
        R = re.sub(r"\?", str(i), result)   
        try:
            L = eval(L)
        except: #e.g. "00604 * 34" #Handle leading 0s on L (just )
            continue
        # Handle R(esult) if == 00: (can't be, skip in loop)
        if int(R) == 0 and len(str(R)) > 1:
            continue #answer can't be '00(0...)'!
            
        #FINAL CHECK: WHAT IS THE ? NUMBER?
        if L == int(R):
            if str(i) in num1 or str(i) in num2 or str(i) in result: #?RUNE number can't be a number in the rest of the equation
                continue
            else: #YAY!
                return i
        else:
            pass
    return -1 # No possible answer

"""
    You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system, and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators, but he needs your help to figure out the rest.
The professor will give you a simple math expression, of the form
        [number][op][number]=[number]
    He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-), and multiplication (*), so those are the only ones that will appear. Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s. If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator, and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.
    Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.
    Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such rune exists.
>>>        test.assert_equals(solve_runes("??*??=302?"), 5, "Answer for expression '??*??=302?' ");
>>>        test.assert_equals(solve_runes("?*11=??"), 2, "Answer for expression '?*11=??' ");
>>>        test.assert_equals(solve_runes("??*1=??"), 2, "Answer for expression '??*11=??' ");
"""
