class Solution:
    
    def longestCommonPrefix(self,words):
        """Find the shortest & longest words ONLY, then compare letter by letter. 
        When you hit an incongruence, stop!"""
        # [flower, flow, fly]
        short, long = min(words), max(words) # fly, flower
        i = 0
        while i < len(short):
            print(short[i], long[i])
            if short[i] != long[i]:
                short = short[:i]
                break
            i +=1
        return short
    
    def _longestCommonPrefix(self, words: List[str]) -> str:
        prefix = ""
        #--Dole out single elem of each item 1-at-a-time: ('f','f','f'), ('l',''l','l')...
        for x in zip(*words):
            temp = set(x)
            if len(temp) != 1:
                break
            else:
                prefix += x[0]
        return prefix
                
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
  Input: strs = ["flower","flow","flight"]
  Output: "fl"
Example 2:
  Input: strs = ["dog","racecar","car"]
  Output: ""
    Explanation: There is no common prefix among the input strings.

"""
