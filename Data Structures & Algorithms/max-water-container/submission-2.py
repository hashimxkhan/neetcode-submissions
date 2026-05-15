class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l = 0
        h = len(heights) - 1
        while l < h:
            most = max(most, min(heights[l], heights[h]) * (h-l))
            if heights[l] < heights[h]:
                l+=1
            else:
                h-=1
        return most