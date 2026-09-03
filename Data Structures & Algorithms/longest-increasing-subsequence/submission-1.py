class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #

        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(nums):
                return 1
            best = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    cur = 1 + dp(j)
                    best = max(cur, best)
            memo[i] = best
            return best
        
        best = 1
        for i in range(len(nums)):
            cur = dp(i)
            best = max(cur, best)
        return best
