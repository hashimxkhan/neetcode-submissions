class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(i, curCost):
            if i >= len(cost):
                return curCost
            curCost+= cost[i]
            return min(dfs(i+1, curCost), dfs(i+2, curCost))
        return min(dfs(0, 0), dfs(1,0))