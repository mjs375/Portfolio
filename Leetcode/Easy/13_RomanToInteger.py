class Solution:
    def romanToInt(self, s:str) -> int:
        s = s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX")
        s = s.replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")
        value = 0
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,}
        for symbol in s:
            value += values[symbol]
        return value
        
        
    def NAIVE_romanToInt(self, s: str) -> int:
        value = 0
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,}
        for i in range(len(s)):
            print(s[i])
            #--Handle last symbol:
            if i == len(s)-1:
                value += values[s[i]]
            #--Handle 'I' for '4' and '9':
            elif s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                value -= 1
            #--Handle 'X' for '40' and '90':
            elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                value -= 10
            #--
            elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                value -= 100
            #--Add numerals value as usual:
            else:
                value += values[s[i]]
        print(f"Value: {value}")
        return value




"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

  I can be placed before V (5) and X (10) to make 4 and 9. 
  X can be placed before L (50) and C (100) to make 40 and 90. 
  C can be placed before D (500) and M (1000) to make 400 and 900.
  Given a roman numeral, convert it to an integer.

  Input: s = "MCMXCIV"
  Output: 1994
  Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
