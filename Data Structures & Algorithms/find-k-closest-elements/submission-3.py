class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        best = float('inf')
        ind = -1
        for i in range(len(arr)):
            if (abs(arr[i] - x) < best):
                best = abs(arr[i] - x)
                ind = i

        l = ind-1
        r = ind+1
        res = []
        res.append(arr[ind])
        while True:
            if len(res) == k or (r >= len(arr) and l < 0):
                return sorted(res)
            if r >= len(arr) and l >= 0:
                res.append(arr[l])
                l-=1
                continue
            if r < len(arr) and l < 0:
                res.append(arr[r])
                r+=1
                continue
            if (abs(arr[r] - x) < abs(arr[l] - x)):
                res.append(arr[r])
                r+=1
            else:
                res.append(arr[l])
                l-=1
        
            