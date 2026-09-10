class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = []
        for s in strs:
            sort = sorted(s)
            new.append(sort)
        
        maps = {}
        ret = []
        for i, s in enumerate(new):
            if tuple(s) not in maps:
                maps[tuple(s)] = []
            maps[tuple(s)].append(i)
        
        for key in maps:
            anagrams = maps[key]
            cur = []
            for num in anagrams:
                cur.append(strs[num])
            ret.append(cur)
        return ret
                