class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(i, target):
            if target < 0 or i >= len(coins):
                return float('inf')
            if target == 0:
                return 0
            if (i,target) in memo:
                return memo[(i,target)]
            
            memo[(i,target)] = min(1 + dp(i, target - coins[i]), dp(i+1, target))
            return memo[(i,target)]
            
        minCoins = float('inf')
        for i in range(len(coins)):
            num = dp(i, amount)
            minCoins = min(num, minCoins)
        if minCoins == float('inf'):
            return -1
        else:
            return minCoins