class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = float('inf')
        best = 0
        for price in prices:
            curMin = min(curMin, price)
            best = max(best, price - curMin)
        return best