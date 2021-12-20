class Solution:
    # Can nums repeat? IDK yet...
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range (1, len(s)+2):
            if i not in s:
                return i



"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
  Input: nums = [1,2,0]
  Output: 3

Example 2:
  Input: nums = [3,4,-1,1]
  Output: 2

Example 3:
  Input: nums = [7,8,9,11,12]
  Output: 1
"""
