class Solution:
    def convertToTitle(self, col: int) -> str:
        
        ans = ""
        
        # Continue decrementing 'col':
        while col > 0:
            print(col, ans)
            
            temp = col % 26 # get remainder after 26
            
            # Do we need to roll-over Z=>A
            if temp == 0: # 
                temp = 26
                col -= 1
            
            ans = chr( 64 + temp ) + ans
            col = col//26
            
        return ans
"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
  For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

  Example 1:
    Input: columnNumber = 1
    Output: "A"
    
  Example 2:
    Input: columnNumber = 28
    Output: "AB"
    
  Example 3:
    Input: columnNumber = 701
    Output: "ZY"
"""
