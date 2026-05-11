class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dp(i): # starting at house i return the max amount of money you can rob without robbing adj houses
            if i >= n:
                return 0
            if i == n-1:
                return nums[n-1]
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dp(i+2), dp(i+1))
            return memo[i]
        
        return max(dp(0), dp(1))