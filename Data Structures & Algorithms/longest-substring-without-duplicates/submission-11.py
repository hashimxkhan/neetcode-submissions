class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maps = {}
        l = 0
        best = 0
        for r in range(len(s)):
            if s[r] not in maps:
                maps[s[r]] = r
                best = max(best, len(maps))
            else:
                ind = maps[s[r]]
                while l <= ind:
                    if s[l] in maps:
                        del maps[s[l]]
                        l+=1
                maps[s[r]] = r
        return best
