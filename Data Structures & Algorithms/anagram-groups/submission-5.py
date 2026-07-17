class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = []
        for s in strs:
            sort = sorted(s)
            new.append(sort)
        print(new)

        ret = []
        maps = {}
        for i in range(len(strs)):
            tup = tuple(new[i])
            if tup not in maps:
                maps[tup] = []
            maps[tup].append(i)
        
        print(maps)
        for key in maps:
            arr = maps[key]
            cur = []
            for i in arr:
                cur.append(strs[i])
            ret.append(cur)
        return ret
                