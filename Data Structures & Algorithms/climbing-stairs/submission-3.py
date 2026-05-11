class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dp(i): 
            if i > n:
                return 0
            if i == n:
                return 1
            if cache[i] != -1:
                return cache[i]
            cache[i] = dp(i+1) + dp(i+2)
            return cache[i]

        return dp(0)

        
