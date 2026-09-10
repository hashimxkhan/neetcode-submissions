class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        best = 0
        for num in sets:
            if num-1 not in sets:
                cur = 1
                while num+1 in sets:
                    cur+=1
                    num+=1
                best = max(best, cur)
        return best

             
