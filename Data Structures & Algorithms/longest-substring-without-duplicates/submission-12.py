class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maps = set()
        l = 0
        best = 0
        for r in range(len(s)):
            while s[r] in maps:
                maps.discard(s[l])
                l+=1
            maps.add(s[r])
            best = max(best, len(maps))
        
        return best
          
