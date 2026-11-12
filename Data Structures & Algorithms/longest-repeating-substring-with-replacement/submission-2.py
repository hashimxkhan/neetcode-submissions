class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set()
        for c in s:
            chars.add(c)
        res = 0
        for c in chars:
            l = 0
            ct = 0
            for r in range(len(s)):
                if s[r] == c:
                    ct+=1
                while (r - l + 1) - ct > k:
                    if s[l] == c:
                        ct-=1
                    l+=1
                res = max(res, r - l + 1)
        return res
                
