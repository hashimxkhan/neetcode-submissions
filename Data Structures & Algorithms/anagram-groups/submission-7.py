class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord("a")]+=1
            if tuple(arr) not in maps:
                maps[tuple(arr)] = []
            maps[tuple(arr)].append(s)
        return list(maps.values())