class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minHeights = [0] * len(height)
        curMax = 0
        for i in range(len(height)):
            maxLeft[i] = curMax
            if height[i] > curMax:
                curMax = height[i]
        curMax = 0
        for i in range(len(height)-1, -1, -1):
            maxRight[i] = curMax
            if height[i] > curMax:
                curMax = height[i]

        for i in range(len(height)):
            minHeights[i] = min(maxRight[i], maxLeft[i])
        
        res = 0
        for i in range(len(height)):
            curWater = minHeights[i] - height[i]
            if curWater > 0:
                res+=curWater
        return res
            
        
        