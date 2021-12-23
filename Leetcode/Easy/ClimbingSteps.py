class Solution:
    memo  = {1:1,2:2,3:3}
    def climbStairs(self, n: int) -> int:
        """Recursive + memoization"""
        print(n)
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.memo:
            return self.memo[n] # memoization
        else:
            temp = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.memo[n]=temp
            return temp
        
        
    @cache # @functools.cache
    def __climbStairs(self, n):
        """@cache decorator automatically caches in a dictionary function INPUTS as key
        and function outputs as value and so when you call function with a previously stored key
        it doesn't actually run the function, it just looks it up quickly."""
        print(n)
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
    #@cache
    def _climbStairs(self, n):
        """Correct solution, but times out."""
        print(n)
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    
    
"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    Example 1:
      Input: n = 2
      Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps
    Example 2:
      Input: n = 3
      Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
"""
    
    

"""
`n` steps can be reached from either (n-1) or (n-2) steps: 
    ways(n) = ways(n-1) + ways(n-2)
SO Recurse down... (n-1) steps can be reached, too, from:
    (n-1) or (n-2)     if we rename (n-1) from above as `n`
SO keep going down, down... until the base cases of
    n=1 / n=2

"""
