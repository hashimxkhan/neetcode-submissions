class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > minPrice:
                best = max(best, prices[i] - minPrice)
            else:
                minPrice = prices[i]
        return best