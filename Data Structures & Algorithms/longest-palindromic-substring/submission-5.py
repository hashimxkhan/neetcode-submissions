class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        maxRes = ""
        for i in range(len(s)):
            r, l = i, i
            res = ""
            # even 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            
            #odd
            r = i+1
            l = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            if len(res) > len(maxRes):
                maxRes = res
        return maxRes
            