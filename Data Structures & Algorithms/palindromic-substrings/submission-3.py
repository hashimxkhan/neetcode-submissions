class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                l,r = i, j
                while l < r and s[l] == s[r]:
                    r-=1
                    l+=1
                if l >= r:
                    total+=1
        return total