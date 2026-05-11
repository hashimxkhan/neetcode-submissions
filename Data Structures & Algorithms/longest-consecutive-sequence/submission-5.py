class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)
        
        best = 0
        for num in hashset:
            i = 1
            while  num + 1 in hashset:
                i+=1
                num+=1
            best = max(best, i)
        
        return best

