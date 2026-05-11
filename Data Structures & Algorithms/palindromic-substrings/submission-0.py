class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def palindrome(l,r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
            return res
        
        total = 0
        for i in range(len(s)):
            total+= palindrome(i,i)
            total+= palindrome(i,i+1)
        return total