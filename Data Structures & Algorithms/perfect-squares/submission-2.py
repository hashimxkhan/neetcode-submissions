import sys
sys.setrecursionlimit(100000)
class Solution:
    def numSquares(self, n: int) -> int:

        memo = {}
        def dp(left):
            if left == 0:
                return 0
            if left in memo:
                return memo[left]
            best = float('inf')
            i = 1
            while i * i <= left:
                best = min(best, 1 + dp(left - (i*i)))
                i+=1
            
            memo[left] = best
            return memo[left]
        return dp(n)