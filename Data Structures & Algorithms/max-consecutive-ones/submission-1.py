class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur+=1
                best = max(best, cur)
            else:
                cur = 0
        return best
            