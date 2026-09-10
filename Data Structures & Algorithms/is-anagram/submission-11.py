class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for c in s:
            if c not in hashS:
                hashS[c] = 0
            hashS[c]+=1
        
        for c in t:
            if c not in hashT:
                hashT[c] = 0
            hashT[c]+=1
        
        return hashS == hashT