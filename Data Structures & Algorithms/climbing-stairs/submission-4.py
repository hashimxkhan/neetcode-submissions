class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dp(i): # starting at i count the number of ways we can get to n
            if i > n:
                return 0
            if i == n:
                return 1
            if i in cache:
                return cache[i]
            
            cache[i] = dp(i+1) + dp(i+2)
            return cache[i]
        return dp(0)