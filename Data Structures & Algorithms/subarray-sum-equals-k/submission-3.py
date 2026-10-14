class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force
        cur = 0
        maps = { 0 : 1}
        res = 0
        for num in nums:
            cur+=num
            diff = cur - k
            if diff in maps:
                res+= maps[diff]
            
            if cur not in maps:
                maps[cur] = 0
            maps[cur] = 1 + maps[cur]
        return res
