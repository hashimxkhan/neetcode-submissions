class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        r = 0
        best = 0
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r+=1
                best = max(best, r - l)
            else:
                while s[r] in window:
                    window.remove(s[l])
                    l+=1
        return best


