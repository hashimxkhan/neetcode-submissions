class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for num in nums:
            if num not in maps:
                maps[num] = 0
            maps[num]+=1
        
        ret = []
        for key in maps:
            ret.append([key, maps[key]])
        
        ret.sort(key=lambda x : -x[1])
        res = []
        for i in range(k):
            res.append(ret[i][0])
        return res