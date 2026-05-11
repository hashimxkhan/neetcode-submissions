class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def maxMoney(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(maxMoney(i+1), nums[i] + maxMoney(i+2))
            return cache[i]
        return maxMoney(0)