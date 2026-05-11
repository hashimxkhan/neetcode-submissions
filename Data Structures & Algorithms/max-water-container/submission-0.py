class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l = 0
        h = len(heights)-1
        while l < h:
            first = heights[l]
            second = heights[h]
            curWater = (min(first, second)) * (h - l)
            maxWater = max(maxWater, curWater)
            if first > second:
                h-=1
            else:
                l+=1
        return maxWater

        