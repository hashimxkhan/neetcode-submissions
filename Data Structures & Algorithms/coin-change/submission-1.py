class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def change(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return 1e9
            if rem in cache:
                return cache[rem]
            res = 1e9
            for coin in coins:
                res = min(res, 1 + change(rem-coin))
            cache[rem] = res
            return res

        minCoins = change(amount)     
        return minCoins if minCoins < 1e9 else -1