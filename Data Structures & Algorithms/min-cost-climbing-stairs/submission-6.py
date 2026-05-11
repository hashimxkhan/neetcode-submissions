class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp(i): # starting at index i return the min cost to get to top
            if i >= n:
                return 0
            if i == n-1:
                return cost[n-1]
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dp(i+1),dp(i+2))
            return memo[i]
            
        return min(dp(0), dp(1))