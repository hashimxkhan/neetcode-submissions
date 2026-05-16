class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(rate):
            hrs = 0
            for bananas in piles:
                hrs+= math.ceil(bananas / rate)
            if hrs > h:
                return False
            return True


        l = 1
        r = sum(piles)
        res = r
        while l <= r:
            m = (l+r) // 2
            if hours(m) == True:
                res = min(res, m)
                r = m-1
            else:
                l = m+1
        return res