class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        ret = []
        def bt(remaining, arr):
            if not remaining:
                if tuple(arr) not in seen:
                    ret.append(arr.copy())
                    seen.add(tuple(arr))
                return
            
            for i in range(len(remaining)):
                arr.append(remaining[i])
                bt(remaining[:i] + remaining[i+1:], arr)
                arr.pop()        
        bt(nums,[])
        return ret
