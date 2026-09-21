class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        cur = float('inf')
        for i in range(len(prices)):
            if cur > prices[i]:
                cur = prices[i]
            else:
                total+= (prices[i] - cur)
                cur = prices[i]
        return total