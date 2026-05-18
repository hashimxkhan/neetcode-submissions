class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        total = nums[l]
        best = float('inf')
        while l <= r and r < len(nums):
            if total < target:
                r+=1
                if r == len(nums):
                    break
                total+= nums[r]
            else:
                while total >= target:
                    best = min(best, r - l + 1)
                    total-= nums[l]
                    l+=1
        if best == float('inf'):
            return 0
        return best







