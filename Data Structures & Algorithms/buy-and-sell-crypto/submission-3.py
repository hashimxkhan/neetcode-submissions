class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        best = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                if buy < prices[j]:
                    best = max(best, prices[j] - buy)
        return best