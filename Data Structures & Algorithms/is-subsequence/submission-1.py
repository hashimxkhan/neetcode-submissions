class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        count = 0
        cur = s[count]
        for c in t:
            if c == cur:
                count+=1
                if count >= len(s):
                    return True
                cur = s[count]
        return count >= len(s)