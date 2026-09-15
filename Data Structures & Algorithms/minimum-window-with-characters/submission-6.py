class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapT = {}
        for c in t:
            if c not in mapT:
                mapT[c] = 0
            mapT[c]+=1
        
        l,r = 0,0
        maps ={}
        best = float('inf')
        ret = ""
        have = 0
        while r < len(s):
            if s[r] in mapT:
                mapT[s[r]]-=1
                if mapT[s[r]] >= 0:
                    have+=1
            while have >= len(t):
                if r - l < best:
                    ret = s[l:r+1]
                    best = r - l
                if s[l] in mapT:
                    mapT[s[l]]+=1
                    if mapT[s[l]] > 0:
                        have-=1
                l+=1
            r+=1
        return ret
                