class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set()
        for num in nums:
            sets.add(num)

        best = 0
        for num in nums:
            cur = 1
            if num-1 not in sets:
                while num + 1 in sets:
                    cur+=1
                    num+=1
            best = max(cur, best)
        return best
                
