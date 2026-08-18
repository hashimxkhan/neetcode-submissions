class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        maps = {}
        for num in nums:
            if num not in maps:
                maps[num] = 0
            maps[num]+=1
        
        ret = []

        for key in maps:
            cur = (maps[key], key)
            ret.append(cur)
        ret.sort(key=lambda x: (x[0], -x[1]))
        print(ret)
        retur = []
        for c in ret:
            num, val = c
            for _ in range(num):
                retur.append(val)
        return retur
