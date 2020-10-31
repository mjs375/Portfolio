def next_bigger(n):
    nums = [digit for digit in str(n)]
    a,b = len(nums), 0
    # # # Check is number is already highest it can be:
    for i, v in enumerate(nums):
        try:
            if nums[i] >= nums[i+1]:
                b += 1
        except: pass
    if a-1 == b: # number is highest it can be...
        return -1
    #
    #
    #
    for i,v in enumerate(nums): #find largest R-half in descending order
        try:
            if nums[i-1] > nums[i]:
                breakpoint = i+1 #reset breakpoint
        except: pass 
    print(nums, "|",breakpoint)
    

    
    string = ''.join([str(elem) for elem in nums]) 
    print(string)
    
    if breakpoint == len(str(string)):
        breakpoint = len(str(string)) -1
        print("Success?")
    
    L = string[:breakpoint]
    R = string[breakpoint:]
    print(L,"|",R)
    

"""
  Sequence: 34722641
1. Split the seq in half, such that the R is as long as possible while remaining in decreasing order.
  34722 641
2. Select the last digit of the L half:
  3472(2) 641
3. Find the smallest digit in the R half larger than it
  3472(2) 6(4)1
4. Swap them
  3472(4) 6(2)1
5. Sort the R half into increasing order:
  34724 126 ==> 34724126 !!!
  
e.g. 4312
  431 2
  432 1 => 4321
e.g. 2017
  201 7 
  207 1




"""
    
    
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     
# int("".join(sorted(str(n), reverse=True)))
  # This would return the HIGHEST POSSIBLE number from the digits
    # The kata calls for the NEXT HIGHEST...
