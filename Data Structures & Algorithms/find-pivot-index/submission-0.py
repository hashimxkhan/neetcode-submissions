class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = 0
        for i in range(len(nums)):
            if (total - nums[i]) / 2 == cur:
                return i
            cur+=nums[i]
        return -1