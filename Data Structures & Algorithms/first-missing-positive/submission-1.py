class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        cur = 1
        for num in nums:
            if num > 0 and num == cur:
                cur+=1
        return cur

        

        
