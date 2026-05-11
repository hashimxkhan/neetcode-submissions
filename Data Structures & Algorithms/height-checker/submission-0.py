class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cpy = heights.copy()
        cpy.sort()
        count = 0
        for i in range(len(cpy)):
            if cpy[i] != heights[i]:
                count+=1
        return count