class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}
        def coinChange(i, rem):
            if (i,rem) in cache:
                return cache[(i,rem)]
            if rem == 0:
                return 1
            if rem < 0 or i >= len(coins):
                return 0
            cache[(i,rem)] = coinChange(i+1,rem)
            cache[(i,rem)]+=coinChange(i,rem-coins[i])
            return cache[(i,rem)]
        return coinChange(0, amount)