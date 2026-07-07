class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        cur = nums[0]
        for i in range(len(nums)):
            if nums[i] < cur:
                inc = False
            if nums[i] > cur:
                dec = False
            cur = nums[i]
        
        return inc or dec