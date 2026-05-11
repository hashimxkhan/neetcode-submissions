class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        best = 0
        for i in range(len(nums)):
            cur = 1
            num = nums[i]
            while num+1 in my_set:
                cur+=1
                num+=1
            best = max(cur, best)
        return best

            
        
