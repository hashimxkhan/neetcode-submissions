class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        ret = []
        used = [0] * len(nums)
        def bt(arr):
            if len(arr) == len(nums) and tuple(arr) not in seen:
                ret.append(arr[:])
                seen.add(tuple(arr[:]))
                return
            
            for i in range(len(nums)):
                if used[i]: # if this index is already included in current arr
                    continue
                used[i] = 1
                arr.append(nums[i])
                bt(arr)
                used[i] = 0
                arr.pop()
        bt([])
        return ret
