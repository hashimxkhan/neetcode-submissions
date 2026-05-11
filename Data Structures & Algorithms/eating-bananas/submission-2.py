class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse = True)
        r = piles[0]
        l = 1
        res = r
        while l <= r:
            k = (l + r) // 2
            curH = h
            hours = 0
            for i in range(len(piles)):
                hours+=math.ceil(float(piles[i]) / k)
            
            if hours > h:
                l = k+1
            else:
                res = k
                r = k-1
        return res
                

        