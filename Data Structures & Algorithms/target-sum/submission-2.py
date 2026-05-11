class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} # i, curSum
        def dfs(i, cur):
            if (i, cur) in cache:
                return cache[(i,cur)]
            if i == len(nums):
                if cur == target:
                    return 1
                else:
                    return 0 
            cache[(i,cur)] = (dfs(i+1, cur-nums[i]) + dfs(i+1, cur+nums[i]))
            return cache[(i,cur)]
        return dfs(0,0)
