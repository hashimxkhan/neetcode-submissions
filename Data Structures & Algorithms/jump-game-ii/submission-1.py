class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return float('inf')
            
            if i == len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            best = float('inf')
            for j in range(1, nums[i] + 1):
                best = min(best, 1 + dp(i+j))
            memo[i] = best
            return best
        return dp(0)