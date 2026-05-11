import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBananas = max(piles)
        l = 1
        r = maxBananas + 10
        while l <= r:
            m = (l + r) // 2
            count = self.check(piles, m)
            if count <= h:
                r = m - 1
            elif count > h:
                l = m + 1
        return l




    def check(self, piles, rate):
        count = 0
        for pile in piles:
            count+= math.ceil(pile/rate)            
        return count
            
