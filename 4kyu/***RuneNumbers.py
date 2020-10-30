import re
def solve_runes(runes):
    print(runes,type(runes))
    
    #string = "4+46=101/234*234-23"
    numlist = re.split('[+\-*/=]',runes)
    print(numlist) 
    
    #HANDLE NEGATIVE SIGNS: PUT BACK IN IF A SPACE IN THE LIST OF SPLITS
    for i, elem in enumerate(numlist):
        print(i, elem)
        try:
            if numlist[i-1] == "":
                #numlist[i] = int(elem)*(-1)
                numlist[i] = '-' + numlist[i]
        except: pass

    #Remove spaces from list:
    #[x for x in a if x != [1, 1]]
    nums = [num for num in numlist if num != ""]
    print(nums)
    
    num1 = nums[0]
    num2 = nums[1]
    result = nums[2]
    op = #use regex match instead of split like above to determine operation
    
    
    
    
    pass

# use regex to find '?' and loop-replace them with 0-9,
    # then use eval(...) to check 'num1 op num2 = result'.
