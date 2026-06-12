class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append((0, heights[0]))
        best = 0
        for i in range(1, len(heights)):
            last = i
            while stack and heights[i] < stack[-1][1]:
                val = stack.pop()
                width = i - val[0]
                best = max(best, width * val[1])
                last = val[0]
            stack.append((last, heights[i]))
        while stack:
            val = stack.pop()
            width = len(heights) - val[0]
            best = max(best, width * val[1])
        return best

