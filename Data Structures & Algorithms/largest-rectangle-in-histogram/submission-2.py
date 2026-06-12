class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        for i, height in enumerate(heights):
            l = i-1
            r = i+1
            cur = 1
            while l >= 0 and heights[l] >= height:
                cur+=1
                l-=1
            while r < len(heights) and heights[r] >= height:
                cur+=1
                r+=1
            area = height * cur
            best = max(best, area)
        return best

                






        