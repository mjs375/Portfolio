class Solution:
    def reverseString(self, s: List[str]) -> None:
        """Do not return anything, modify s in-place instead."""
        #--91.30% / 44.18%
        return s.reverse()
        
        """
        #--SLOW:
        for i in range(1,len(s)):
            x = s.pop(0)
            s.insert(-i, x)
        s.insert(0,s.pop())
        return s
        """
"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
  Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
"""
