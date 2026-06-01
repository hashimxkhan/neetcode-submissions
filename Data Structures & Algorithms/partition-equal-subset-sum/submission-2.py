class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        memo = {}
        total = sum(nums)
        def dp(i, curr):
            if i >= len(nums):
                return False
            
            if curr == total - curr:
                return True
            memo[(i,curr)] = dp(i+1, curr + nums[i]) or dp(i+1, curr)
            return memo[(i,curr)]
        
        return dp(0, 0)
            
            
            