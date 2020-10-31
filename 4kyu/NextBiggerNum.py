def next_bigger(n):
    nums = [digit for digit in str(n)] #list-ify the string
    #
    # Is the list already in decreasing order? (no larger number?):
    c = 0 #counter
    for i in range(1,len(str(n)),1): #iterator
        #print(nums[i],i)
        if nums[i-1] >= nums[i]: #check if decreasing order
            c += 1
        if nums[i-1] < nums[i]: #ID the breakpoint
            breakpoint = i
    if c == len(str(n)) - 1:
        return -1 # LARGEST NUM ALREADY
    #
    #
    #
    #
    #
    print(nums, breakpoint)
    L = str(n)[:breakpoint] # Split string...
    R = str(n)[breakpoint:]
    print(L,"|",R)
    #
    #
    L_end = L[-1] # Get last digit of L-half
    #    
    # Get next larger number than L_end:
    R_end = 9
    for digit in R:
        if int(digit) > int(L_end):
            if int(digit) < int(R_end):
                R_end = digit
    # Swap L_end and R_end:
    L = L[:-1] + str(R_end) #new L-string, with R-end
    print(L)
    R = R.replace(str(R_end),L_end,1)
    print(R)
    R=sorted(R)
    R = "".join(R)
    print(R)
    answer = L+R
    print(int(answer))
    return int(answer)




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
