class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        cur = 0
        best = float('inf')
        for r in range(len(nums)):
            cur+=nums[r]
            while cur >= target:
                best = min(r-l+1, best)
                cur-=nums[l]
                l+=1       

        if best == float('inf'):
            return 0
        return best 