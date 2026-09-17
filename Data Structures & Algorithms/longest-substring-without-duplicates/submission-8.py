class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        best = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                best = max(best, len(seen))
            else:
                while s[r] in seen:
                    seen.discard(s[l])
                    l+=1
                seen.add(s[r])
                r+=1
        return best

