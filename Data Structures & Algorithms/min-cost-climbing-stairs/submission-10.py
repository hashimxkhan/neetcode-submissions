class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {}
        def dp(i):
            if i in cache:
                return cache[i]
            if i >= len(cost):
                return 0
            
            if i == len(cost)-1 or i == len(cost)-2:
                cache[i] = cost[i]
                return cache[i]
            
            cache[i] = cost[i] + min(dp(i+1), dp(i+2))
            return cache[i]
        return min(dp(0), dp(1))
            
            
            
        
