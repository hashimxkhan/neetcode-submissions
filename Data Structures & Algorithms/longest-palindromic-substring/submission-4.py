class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                l = i
                r = j
                while l < r and s[l] == s[r]:
                    l+=1
                    r-=1
                
                if l >= r and len(res) < (j-i+1):
                    res = s[i:j+1]
        return res


            