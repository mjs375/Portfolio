class Solution:
    def addSpaces(self, s, spaces):
        """Times out."""
        res = []
        for i, char in enumerate(s):
            if i in spaces:
                res.append(" ")
            res.append(char)
        return "".join(res)
    
    
    def _addSpaces(self, s: str, spaces: List[int]) -> str:
        """Times out."""
        tally = 0
        for i in spaces:            
            s = s[:i+tally] + " " + s[i+tally:]
            tally += 1
        return s
      
"""
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.
  For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
    Return the modified string after the spaces have been added.

Example 1:
  Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
  Output: "Leetcode Helps Me Learn"
  Explanation: 
    The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
    We then place spaces before those characters.

"""
