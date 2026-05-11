class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rightMax = 0 
        maxProfit = 0
        for i in range(len(prices)-1,-1,-1):
            profit = rightMax - prices[i]
            rightMax = max(rightMax, prices[i])
            maxProfit = max(maxProfit, profit)
        return maxProfit
            

        