class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """Naive soln. Time: 55% / Memory:69%."""
        
        n = bin(n)[2:]
        
        swap = {"1":"0", "0":"1"}
        new = ""
        for i in range(len(n)):
            new += swap[n[i]]
        
        return int(new,2)
        
"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
  For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
    Given an integer n, return its complement.
    
  Example 1:
    Input: n = 5
    Output: 2
      Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
"""
