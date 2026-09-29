class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        for a in arr:
            cur = abs(a - x)
            res.append([cur, a])
        res.sort(key =lambda x: (x[0], x[1]))
        ret = []
        for i in range(k):
            ret.append(res[i][1])
        return sorted(ret)