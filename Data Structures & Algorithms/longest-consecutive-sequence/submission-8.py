class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        seq = set()
        for num in nums:
            seq.add(num)
        
        best = 1
        for num in seq:
            cur = 1
            while num+1 in seq:
                cur+=1
                best = max(best, cur)
                num+=1
        
        return best
