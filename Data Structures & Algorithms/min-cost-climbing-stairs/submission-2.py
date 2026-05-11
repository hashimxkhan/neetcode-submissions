class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       
        def minCost(i):
            if i >= len(cost):
                return 0
            return min(cost[i] + minCost(i+1), cost[i] + minCost(i+2))
        return min(minCost(0), minCost(1))