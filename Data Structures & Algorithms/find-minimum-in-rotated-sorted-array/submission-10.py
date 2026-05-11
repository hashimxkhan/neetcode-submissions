class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        if nums[0] < nums[length-1]: # sorted
            return nums[0]
        
        r = length - 1
        l = 0
        
        while l < r:
            m = (l+r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]