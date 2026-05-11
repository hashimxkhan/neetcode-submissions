class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        def count(l,r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1

        for i in range(len(s)):
            # even
            count(i,i)
            #odd
            count(i,i+1)
        return res