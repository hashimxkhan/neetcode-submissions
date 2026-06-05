class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ret = []
        arrs = set()
        def bt(i, arr):
            if i > n+1:
                return
            
            if len(arr) == k:
                if tuple(arr) not in arrs:
                    ret.append(arr.copy())
                    arrs.add(tuple(arr))
            arr.append(i)
        
            bt(i+1, arr)
            arr.pop()
            bt(i+1, arr)
        
        for i in range(1, n+1):
            bt(i, [])

        return ret

                