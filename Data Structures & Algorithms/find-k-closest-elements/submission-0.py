class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        scores = []
        for a in arr:
            scores.append((abs(a-x), a))
        
        scores.sort(key=lambda x: (x[0], x[1]))
        ret = []
        for i in range(k):
            ret.append(scores[i][1])
        ret.sort()
        return ret
