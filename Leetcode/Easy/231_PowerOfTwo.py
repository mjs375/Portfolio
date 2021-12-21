import math
class Solution:
    
    def isPowerOfTwo(self,n):
        if n <= 0:
            return False
        b = str(bin(n))[2:]
        if b.count("1") == 1:
            return True
        else:
            return False
    
    
    def _2_isPowerOfTwo(self,n):
        if n <= 0:
            return False
        hmm = math.log2(n)
        print(hmm)
        if hmm % 1 == 0:
            return True
        else:
            return False
    
    
    def _1_isPowerOfTwo(self, n: int) -> bool:
        """Naive."""
        i = 0
        while True:
            temp = 2**i
            if temp == n:
                return True
            if temp > n:
                return False
            i += 1


"""
Given an integer n, return true if it is a power of two. Otherwise, return false. 
An integer n is a power of two, if there exists an integer x such that n == 2x.
  Example 1:
    Input: n = 1
    Output: true
      Explanation: 20 = 1
  Example 2:
    Input: n = 16
    Output: true
      Explanation: 24 = 16
"""
