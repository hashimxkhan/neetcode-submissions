class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        cache[len(s)] = 1
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i+1 < len(s) and i+1 in cache:
                res = cache[i+1]
            res = dfs(i+1)
            if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                if i+ 2 < len(s) and i+2 in cache:
                    res+= cache[i+2]
                res+=dfs(i+2)
            return res
        return dfs(0)
                    
            