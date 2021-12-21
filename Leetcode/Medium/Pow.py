class Solution:
    """GD I solved it all myself, got stuck a moment on negatives but then I was Error Timeout! GRrr..."""
    
    def myPow(self,x,n):  
        #--BASE CASES:
        if x == 0: return 0
        if n == 0 or x == 1: return 1
        if n == 1: return x
        if n == -1: return 1/x
        
        if n % 2 == 0:
            return self.myPow(x, n//2) ** 2
        else:
            return self.myPow(x, n//2) * self.myPow(x, (n//2) + 1)
    
    
    
    
    def _1_myPow(self,x,n):
        if x == 0: # edge case
            return 1
        if n == 0: # base condition
            return 1
        if n > 0:
            if n % 2 == 1:
                return x * self.myPow(x,n//2) * self.myPow(x,(n//2))
            return self.myPow(x,n//2) * self.myPow(x,(n//2))
        elif n < 0:
            if abs(n) % 2 == 1:
                return x / self.myPow(x,n//2) / self.myPow(x,(n//2))
            return self.myPow(x,n//2) / self.myPow(x,(n//2))
        
        
        
        
        
    """
2,5
    return 2 * (2,2)* (2,2)
        2,2
            return 2 *
        

"""
        
    
    def ____myPow(self,x,n):
        #--Edge case:
        if x == 0:
            return 1
        #--Bottom of recursive well:
        if n == 0:
            return 1
        #--If n is +:
        elif n > 0:
            return x * self.myPow(x,n-1)
        #--If n is -:
        elif n < 0: 
            return self.myPow(x,n+1) / x
 


    

    
    def ___myPow(self,x,n):
        p = 1
        for i in range(n):
            p *= x
        return p
    
    def __myPow(self,x,n):
        print("    ",x,n)
        if n > 1:
            print(f"{x} * self.myPow({x},{n-1})")
            return x * self.myPow(x,n-1)
        elif n < 0:
            print(f"{x} / self.myPow({x},{n-1})")
            return  self.myPow(x,n+1) / 1
        elif n == 1:
            print(f"!{x}")
            return 1
    
    def _myPow(self, x: float, n: int) -> float:
        """Easy!"""
        return x**n
    
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
  Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000
"""
