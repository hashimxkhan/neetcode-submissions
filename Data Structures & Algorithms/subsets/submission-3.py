class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def bt(i, arr):
            if i >= len(nums):
                ret.append(arr[:])
                return
            
            arr.append(nums[i])
            bt(i+1, arr)
            arr.pop()
            bt(i+1, arr)
        
        bt(0, [])
        return ret
        
        
        
