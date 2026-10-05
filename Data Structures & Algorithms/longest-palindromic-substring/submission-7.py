class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.best = 0
        self.ret = ""
        def check(l,r):
            if l < 0 or r >= len(s):
                return
            
            if s[l] == s[r]:
                if self.best < r - l + 1:
                    self.best = r - l + 1
                    self.ret = s[l:r+1]
                l-=1
                r+=1
                check(l,r)
        
        for i in range(len(s)):
            check(i,i)
            check(i,i+1)
        return self.ret