class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS = {}
        hashT = {}
        for i in range(len(s)):
            if s[i] in hashS:
                hashS[s[i]]+= 1
            else:
                hashS[s[i]] = 1
            if t[i] in hashT:
                hashT[t[i]]+= 1
            else:
                hashT[t[i]] = 1
        for i in range(len(s)):
            if s[i] not in hashT:
                return False
            if hashS[s[i]] != hashT[s[i]]:
                return False
        return True
