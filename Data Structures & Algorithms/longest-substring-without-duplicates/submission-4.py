class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0
        curLen = 0
        l = 0
        for i in range(len(s)):
            if s[i] in seen:
                l = max(seen[s[i]] + 1, l)
            seen[s[i]] = i
            res = max(res, i-l+1)
        return res



                

            

        