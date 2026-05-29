class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def robbing(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(robbing(i+1), nums[i] + robbing(i+2))
            return cache[i]
        
        return max(robbing(0), robbing(1))