class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = 0
        for i in range(len(nums)):
            cur = nums[i]
            best = max(cur, best)
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    cur+= nums[j]
                    best = max(cur, best)
                else:
                    break
        return best
