class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        maps = {0: -1}
        cur = 0
        for i in range(len(nums)):
            cur+= nums[i]
            if cur % k in maps and i - maps[cur % k] > 1:
                return True
            if cur % k not in maps:
                maps[cur % k] = i
        return False
            
