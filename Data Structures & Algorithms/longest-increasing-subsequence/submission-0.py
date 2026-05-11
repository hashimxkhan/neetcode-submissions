class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dp(i,j): # length of LIS where i is prev element and j is cur
            if j >= len(nums):
                return 0
            
            LIS = dp(i,j+1) # skip cur

            if i == -1 or nums[i] < nums[j]:
                LIS = max(LIS, 1+ dp(j,j+1))
            
            return LIS
        return dp(-1, 0)
            
