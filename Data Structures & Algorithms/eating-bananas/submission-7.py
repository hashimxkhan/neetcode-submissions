class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 1000000000
        def check(m):
            total = 0
            for p in piles:
                total+= math.ceil(p / m)
            return total <= h

        while l <= r:
            m = (l + r) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l

        