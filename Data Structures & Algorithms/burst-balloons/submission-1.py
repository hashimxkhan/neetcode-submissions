class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        def dp(nums):
            if len(nums) == 0:
                return 0
            best = 0
            if tuple(nums) in memo:
                return memo[tuple(nums)]
            for j in range(len(nums)):
                left = 1
                right = 1
                if j-1 >= 0:
                    left = nums[j-1]
                if j+1 < len(nums):
                    right = nums[j+1]
                best = max(best, nums[j] * left * right + dp(nums[:j] + nums[j+1:]))
            
            memo[tuple(nums)] = best
            return best
        
        return dp(nums)