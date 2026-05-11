class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        for i in range(n+1):
            cur = 0
            j = i
            while j:
                cur+= j & 1
                j = j >> 1
            ret.append(cur)
        return ret

            