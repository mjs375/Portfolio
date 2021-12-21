class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        """Maintain a tally. First time you encounter a num, add it.
        Second time, subtract it. Tally will be the single solo num at end.
        Use a dict to track previously encountered nums."""
        x = {}
        tally = 0
        for num in nums:
            if num not in x:
                x[num] = None
                tally += num
            else:
                tally -= num
        print(tally)
        return tally
    
    
    def _singleNumber(self, nums: List[int]) -> int:
        track = set()
        for num in nums:
            if num in track:
                print("Remove",num)
                track.discard(num)
            else: # only the solo elem will remain
                print("Add",num)
                track.add(num)
        return track.pop()
    



"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
  Example 1:
    Input: nums = [2,2,1]
    Output: 1
"""
