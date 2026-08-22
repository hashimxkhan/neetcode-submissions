class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        diff = 0
        best = 1
        r = 0
        nums.sort()
        for i in range(len(nums)):
            cur = nums[i]
            diff = k
            for j in range(i-1, -1, -1):
                diff = diff - (cur - nums[j])
                if diff < 0:
                    break
                else:
                    best = max(best, i - j+1)
        return best
                
            


