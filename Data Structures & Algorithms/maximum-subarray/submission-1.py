class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxi = nums[0]
        for i in range(len(nums)):
            cur+= nums[i]
            maxi = max(cur, maxi)
            if cur < 0:
                cur = 0
        return maxi                
