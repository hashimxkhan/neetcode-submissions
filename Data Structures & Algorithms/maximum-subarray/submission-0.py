class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        for i in range(len(nums)):
            cur = 0
            for j in range(i,len(nums)):
                cur+= nums[j]
                maxi = max(cur, maxi)
        return maxi
                
