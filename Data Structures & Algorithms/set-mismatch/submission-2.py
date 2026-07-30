class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        maps = {}
        for n in nums:
            if n not in maps:
                maps[n] = 0
            maps[n]+=1
        ret = []
        for i in range(1, len(nums) + 1):
            if i in maps and maps[i] > 1:
                ret.append(i)
        for i in range(1, len(nums) + 1):
            if i not in maps:
                ret.append(i)
        return ret