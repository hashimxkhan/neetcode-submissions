class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cache = {}
        def dp(i):
            if i >= len(nums) - 1:
                return 0
            if i in cache:
                return cache[i]
            best = float('inf')
            for j in range(i+1, i + nums[i] + 1):
                best = min(best, 1 + dp(j))
            cache[i] = best
            return best

        return dp(0)