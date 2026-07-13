class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        cur = nums[0] % 2

        for i in range(1, len(nums)):
            if nums[i] % 2 == cur:
                return False
            cur = nums[i] % 2
        
        return True