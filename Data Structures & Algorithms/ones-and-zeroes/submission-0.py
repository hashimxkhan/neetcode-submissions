class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        memo = {}

        def dp(i, mCount, nCount):
            if i >= len(strs):
                return 0
            if (i, mCount, nCount) in memo:
                return memo[(i,mCount,nCount)]
            ms = 0
            ns = 0
            for c in strs[i]:
                if c == '0':
                    ms+=1
                else:
                    ns+=1
            if ns + nCount <= n and ms + mCount <= m:
                take = 1 + dp(i+1, mCount + ms, nCount + ns)
                leave = dp(i+1, mCount, nCount)
                memo[(i,mCount,nCount)] = max(take, leave)
                return max(take, leave)
            else:
                memo[(i,mCount,nCount)] = dp(i+1, mCount, nCount)
                return memo[(i,mCount,nCount)]
        
        return dp(0,0,0)
            
