class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dp(i, count):
            if (i,count) in memo:
                return memo[(i,count)]
            if count == len(t):
                return 1
            if i >= len(s):
                return 0
            
            total = dp(i+1, count)
            if s[i] == t[count]:
                total = total + dp(i+1,count+1)
            memo[(i,count)] = total
            return total

        
        dp(0,0)
        return memo[(0,0)]
            
            