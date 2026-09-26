class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}
        def dp(i, cur):
            if cur == 0:
                return 1
            if cur < 0:
                return 0
            if (i,cur) in cache:
                return cache[(i,cur)]
            best = 0
            for j in range(i, len(coins)):
                best+= dp(j, cur - coins[j])
            cache[(i,cur)] = best
            return best
        return dp(0, amount)
