class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def bsta(weights, cap, days):
            ships = 1
            cur = cap
            for w in weights:
                if cur - w < 0:
                    ships+=1
                    if ships > days:
                        return False
                    cur = cap
                cur-= w
            return True
                

        h = sum(weights)
        l = max(weights)
        res = h
        while l <= h:
            m = (l+h) // 2
            if bsta(weights, m, days):
                res = min(res, m)
                h = m-1
            else:
                l = m+1
        return res


        

