class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dp(cur):
            if cur in cache:
                return cache[cur]
            if cur < 0:
                return float('inf')
            if cur == 0:
                return 0
            
            best = float('inf') 
            for coin in coins:
                best = min(best, 1 + dp(cur - coin))
            cache[cur] = best
            return cache[cur]
        
        ret = dp(amount)
        if ret == float('inf'):
            return -1
        return ret