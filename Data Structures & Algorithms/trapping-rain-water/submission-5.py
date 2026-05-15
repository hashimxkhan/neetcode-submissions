class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftmax = 0
        rightmax = height[r]
        water = 0
        while l <= r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])
            if leftmax > rightmax:
                water+= max(0, min(leftmax, rightmax) - height[r])
                r-=1
            else:
                water+= max(0, min(leftmax, rightmax) - height[l])
                l+=1
        return water
            