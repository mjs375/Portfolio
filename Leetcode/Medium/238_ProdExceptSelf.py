class Solution:
    DEBUG = True
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if self.DEBUG: print("Nums:\t",nums,"\n")
        
        ans = [1 for i in nums] # products to-be   O(n)
        
        left = 1
        for i in range(1,len(nums)):   # O(n) => O(2n)
            if self.DEBUG: print(nums[i])
            left *= nums[i-1] # look to left-of
            ans[i] *= left
        if self.DEBUG: print(ans)
        
        right = 1
        for j in range(len(nums)-2,-1,-1): # O(n) => O(3n)
            if self.DEBUG: print(nums[j])
            right *= nums[j+1]
            ans[j] *= right
            
        # Notice the 'blind-spot' of nums[i] in both loops! See below
        
        if self.DEBUG: print("Ans:\t",ans)
        return ans
    """
    [1,               2,               3,               4,               5]
    _*2*3*4*5     1*_*3*4*5        1*2*_*4*5        1*2*3*_*5        1*2*3*4*_
    .                 1               1 2             1 2 3             1 2 3 4
    5 4 3 2          5 4 3            5 4               5                  .
    
        **Notice the blind-spot, nums[i] is missing in both its left-of & right-of products... good!
    
    Create O(3n) soln: a 'left-of' product array and a 'right-of' product array.
        - Leftof [i]
        - Rightof [i]
    Multiple together at end in second loop: O(2n) => approx. O(n)

    
    """



"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

  Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
  Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
"""
