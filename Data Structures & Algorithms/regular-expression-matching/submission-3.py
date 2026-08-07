class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}
        def dp(i,j):
            if j == len(p):
                if i == len(s):
                    return True
                return False

            if (i,j) in memo:
                return memo[(i,j)]

            match = False
            if i < len(s) and (p[j] == s[i] or p[j] == '.'):
                match = True

            if j+1 < len(p) and p[j+1] == '*':
                skip = dp(i, j+2)
                take = match and dp(i+1, j)
                memo[(i,j)] = skip or take
                return memo[(i,j)]

            memo[(i,j)] = match and dp(i+1,j+1)
            return memo[(i,j)]
        
        return dp(0,0)
            
