class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def dp(i, canBuy):
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in cache:
                return cache[(i,canBuy)]

            cooldown = dp(i+1, canBuy)
            if canBuy:
                buying = dp(i+1, False) - prices[i]
            else:
                buying = dp(i+2, True) + prices[i]
            
            cache[(i,canBuy)] = max(cooldown, buying)
            return cache[(i,canBuy)]
        
        return dp(0, True)

            

            


            


            

