class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        """Sum two binary strings.
        Time: 13% / Memory: 55%"""
        
        # Find the longer string, fill up the shorter one to match:
        if len(a) > len(b):
            b = b.zfill( len(a) ) # leading zeroes
        else:
            a = a.zfill( len(b) )
        # Reverse each so we can calc smallest place to largest:
        a,b = a[::-1], b[::-1]
        
        # Vars
        carry = 0 # carry-over var
        new = "" # the new num
        
        for a,b in zip(a,b):
            
            # Anything carried over from last place?
            place = carry
            
            # 1+1=0 (1 carry) | 1+0 = 1 | 0+0=0
            place += 1 if a == '1' else 0
            place += 1 if b == '1' else 0

            # Calc current digits place:
            new = ('1' if place % 2 == 1 else '0') + new
            
            # %2 because 1+1 != 2, but 1 in the next place
            carry = 1 if place >= 2 else 0
            
           
        # If the carry brings forth one last new digits/place:
        if carry != 0:
            new = '1' + new
                
        return new
       
        
    def _addBinary(self, a: str, b: str) -> str:
        """Sum two binary strings using inbuilt bin() & int().
        Time: 78% / Memory: 55%"""
        return bin( int(a,2) + int(b,2) )[2:]
      
      
"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
  Input: a = "11", b = "1"
  Output: "100"
  
Example 2:
  Input: a = "1010", b = "1011"
  Output: "10101"
"""
    
