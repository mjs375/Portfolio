import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Apparently .split() treats whitespaceS as one... convenient..."""
        return len(s.split()[-1])
    
    
    def _lengthOfLastWord(self, s: str) -> int:
        s = re.sub(' +', ' ',s)
        s = s[::-1].strip()
        if " " not in s:
            return len(s)
        num = s.index(" ")
        return num
        



"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
"""
