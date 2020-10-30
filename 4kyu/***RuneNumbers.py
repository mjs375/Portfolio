import re
def solve_runes(runes):
    # # # Split string into nums/signs
    numlist = re.split('[+\-*/=]',runes)
    #
    # # # HANDLE NEGATIVE SIGNS: PUT BACK IN IF A SPACE IN THE LIST OF SPLITS
    for i, elem in enumerate(numlist):
        try:
            if numlist[i-1] == "":
                numlist[i] = '-' + numlist[i]
        except: pass
    #
    # # # Remove spaces from list:
    nums = [num for num in numlist if num != ""]
    #
    num1 = nums[0]
    num2 = nums[1]
    result = nums[2]
    match = re.search('[+\-*/=]',runes[1:])
    op = match[0] #use regex match instead of split like above to determine operation
    #
    ############
    #print("Num1:",num1,"Operation",op,"Num2:",num2,"=","Result:",result)
    # 
    #
    #
    equation = f"{num1}{op}{num2}" #={result} ??? still inside
    #print(equation)
    #
    #
    # # # Loop eval(equation) replacing '?' with 0-9: if True, ?=num
    for i in range(10): #0-9
        L = re.sub(r"\?", str(i), equation) #OR# x = equation.replace("?",str(i))        
        R = re.sub(r"\?", str(i), result)        
        L = eval(L)
        
        

        if R == len(str(R)) * 0 and len(str(R)) > 1:
            print(R)
            continue #answer can't be '00(0...)'!
            
        #FINAL CHECK: WHAT IS THE ? NUMBER?
        if L == int(R):
            return i
        else:
            pass
    return -1
 
