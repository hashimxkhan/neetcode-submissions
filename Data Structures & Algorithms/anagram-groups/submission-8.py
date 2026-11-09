class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord('a') - ord(c)]+=1
            
            tup = tuple(arr)
            if tup not in maps:
                maps[tup] = []
            maps[tup].append(s)
        
        ret = []
        for key in maps:
            ret.append(maps[key])
        return ret
