class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        best = 0
        for i in range(1, len(prices)):
            if prices[i] > curMin:
                best = max(best, prices[i] - curMin)
            else:
                curMin = prices[i]
        return best
