class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = 0
        r = len(height) - 1
        rightMax = height[r]
        leftMax = height[l]
        while l < r:
            if height[l] < height[r]:
                l+=1
                leftMax = max(leftMax, height[l])
                total+= leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                total+= rightMax - height[r]

        return total

        