class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            cur = (l+r) // 2
            hours = 0
            for p in piles:
                hours = hours + (math.ceil(p / cur))
            if hours > h:
                l = cur+1
            else:
                r = cur-1
        return l