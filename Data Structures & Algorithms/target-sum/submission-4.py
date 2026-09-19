class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def dp(i, tot):
            if i >= len(nums):
                if tot == target:
                    return 1
                return 0
            
            if (i,tot) in cache:
                return cache[(i,tot)]
            cache[(i,tot)] = dp(i+1, tot+nums[i]) + dp(i+1, tot-nums[i])
            return cache[(i,tot)]
         
        return dp(0, 0)