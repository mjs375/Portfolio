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


"""
BITWISE OPERATORS

& (AND:logical conjunction): for each pair of bits occupying the same position, 
    it returns a '1' only when both bits are switched on.
            1 0 0 1 1 1 0 0
            0 0 1 1 0 1 0 0
        =>  0 0 0 1 0 1 0 0
    The result is an intersection of the operators' args.
    Arithmetically, this is equivalent to the product of 2 bit values.
    
| (OR:logical disjunction): for each pair of bits,
    it returns a '1' if at least one is switched on.
            1 0 0 1 1 1 0 0
            0 0 1 1 0 1 0 0 
        =>  1 0 1 1 1 1 0 0
    The result is a union of the operator's args. Only 2 0's give a '0'.
    The arithmetic behind this is a combo of a sum and a product of the bit values.

(^) (XOR: exclusive or/exclusive disjunction): simulate it by building atop existing operators.
            def xor(a,b):
                return (a and not b) or (not a and b)
        Evals 2 mutually exclusive conditions and tells you whether 
        exactly one of them is met. 
        E.g. a person can be a child or an adult, but not both!
        It's also not possible for a person to be neither a child nor an adult.
        - Visually, its a symmetric difference of the operators' args.
            - 1+0=1   0+0=0   1+1=>0(!)
~ (NOT: expects just 1 argument): unary bitwise operator. Performs logical negation.
            1 1 0 0 1 0 1 1
       => ~ 0 0 1 1 0 1 0 0
        The inverted bits are a complement to one, which turns 0s=>1s, 1s=>0s.
 
"""
