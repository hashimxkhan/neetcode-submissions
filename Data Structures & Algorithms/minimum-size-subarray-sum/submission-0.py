class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # brute force
        best = float('inf')
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total+= nums[j]
                if total >= target:
                    best = min(best, j - i + 1)
                    break
        if best == float('inf'):
            return 0
        return best



