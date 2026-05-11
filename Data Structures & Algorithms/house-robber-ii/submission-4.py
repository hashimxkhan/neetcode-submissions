class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        def dp(i, start): # starting from i return the max amount of money you can rob without robbing adj houses
            if i >= n:
                return 0
            if i == n-1 and start:
                return nums[i]
            if i == n-1 and not start:
                return 0
            if (i,start) in memo:
                return memo[(i,start)]
            
            memo[(i,start)] = max(nums[i] + dp(i+2, start), dp(i+1, start))
            return memo[(i,start)]
        return max(dp(0, 0), dp(1, 1))