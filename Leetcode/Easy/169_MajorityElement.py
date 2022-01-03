class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Returns the element which appears more than `n/2` times.
        Majority elem assumed to always exist.
        solve in O(n) time and O(1) memory/space.
        Boyer-Moore Algorithm explanation: https://www.youtube.com/watch?v=n5QY3x_GNDg
            => O(2n) time: runs through array twice (actually x1 here, since no step 2 verification)
            => O(1) space: negligible memory usage (not relative to size `n`)
        """
        counter = 0
        candidate = None
        
        #--Step 1: Find candidate element | O(n)
        
        for num in nums:
            
            # If counter reduced to 0,
            if counter == 0:
                # Change out current (potential) candidate
                candidate = num
            
            # Check if num matches current candidate...
            if num != candidate:
                # If not, decrement counter:
                counter -= 1
            else:
                # otherwise, increment counter for current candidate:
                counter += 1
                
            #counter += 1 if num == candidate else -1 # 1-liner
                        
        
        """ NOT NECESSARY: MAJORITY ALWAYS EXISTS per question context
        #--step 2: Verify candidate element | O(n)
        majority = len(nums) / 2
        check = nums.count(candidate)
        if check > majority:
            return candidate
        else:
            return -1
        """
        return candidate
      
      
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
  Input: nums = [3,2,3]
  Output: 3
  
Example 2:
  Input: nums = [2,2,1,1,1,2,2]
  Output: 2
  
"""
