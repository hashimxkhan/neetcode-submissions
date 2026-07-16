class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps = {}
        for c in s:
            if c not in maps:
                maps[c] = 0
            maps[c]+=1

        for i in range(len(s)):
            if maps[s[i]] == 1:
                return i
        return -1