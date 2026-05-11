class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        def minCost(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = min(cost[i] + minCost(i+1), cost[i] + minCost(i+2))
            return cache[i]
        return min(minCost(0), minCost(1))