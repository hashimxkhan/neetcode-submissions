class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        def dp(i):
            if i >= len(nums):
                return 0
            cur = nums[i]
            best = nums[i]
            for j in range(i+1, len(nums)):
                cur = cur * nums[j]
                best = max(best, cur)
            return best
        
        return dp(0)
            