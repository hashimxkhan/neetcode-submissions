class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        def maxMoney(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(maxMoney(i+1), nums[i] + maxMoney(i+2))
            return cache[i]
        return maxMoney(0)
