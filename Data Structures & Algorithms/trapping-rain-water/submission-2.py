class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length <= 2:
            return 0
        l = 0
        h = length - 1
        maxH, maxL = height[h], height[l]
        res = 0
        while l < h:
            if maxH < maxL:
                h-=1
                maxH = max(maxH, height[h])
                res+= maxH - height[h]
            else:
                l+=1
                maxL = max(maxL, height[l])
                res+=maxL - height[l]
        return res

            
        return res



            
        
        