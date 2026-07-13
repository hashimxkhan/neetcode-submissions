class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        maps = {}
        for num in nums:
            if num not in maps:
                maps[num] = 0
            maps[num]+=1
        
        sorte = sorted(maps.items(), key= lambda x: (x[1], -x[0]))
        ret = []
        for item in sorte:
            for _ in range(item[1]):
                ret.append(item[0])
        return ret