class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}

        def dp(i, start):
            if i >= len(nums):
                return 0
            if (i,start) in cache:
                return cache[(i,start)]
            if i == len(nums) - 1:
                if start == 0:
                    return 0
                else:
                    return nums[i]
            
            cache[(i,start)] = max(dp(i+1, start), nums[i] + dp(i+2, start))
            return cache[(i,start)]
        
        return max(dp(0,0), dp(1,1))