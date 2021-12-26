class Solution:
    def search(self, nums, target):
        # Set start/end points (indexes):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Find new midpoint
            mid = (left + right) // 2   # eg 5
            
            # Check if midpoint is target:
            if nums[mid] == target:
                return mid
            
            # elif midpoint is less than target, try again w/ new interval
            elif nums[mid] < target:
                left = mid + 1 # e.g. 0 1 2 _3_ 4 5 6    (t=4)
                
            # elif midpoint greater than target...
            elif nums[mid] > target:
                right = mid - 1
        
        # No target solution possible, list exhausted:
        return -1
        
        

    
    
    def _search(self, nums: List[int], target: int, index=0) -> int:
        """Ew, ugly as hell."""
        print("SEARCH:",nums, "|",target)
        print(f"   {index}")
        
        #--If `nums==[]`, return `-1`
        if not nums: 
            return -1
        if len(nums) == 1 and nums[0] != target:
            return -1
        
        #--Determine pivot:  0 1 2 3 4 5 6 => 
        pivot = len(nums) // 2     # => 3
        
        #--Divide nums in half     0 1 2   3  4 5 6
        left, right = nums[0:pivot], nums[pivot:]
        
        #--Determine middle value:
        middle = nums[pivot]   # 3
        
        #--Check middle value of interval against target value.
        print(f"   {middle} =? {target}")
        if middle == target: # target=3?
            #--If `value==target`, return solution:
            return pivot + index #pivot is rel, index is absolute
        
        #--If `target<value`, run `search()` w/ lower half of interval
        if middle > target:
            print(f"      lower half")
            return self.search(left,target,index)
        
        #--If `target>value`, run `search()` w/ upper half of interval
        if middle < target:
            print(f"      upper half")
            return self.search(right, target, index+pivot)
        
        




"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

  Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
      Explanation: 9 exists in nums and its index is 4
      
  Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
      Explanation: 2 does n
"""
