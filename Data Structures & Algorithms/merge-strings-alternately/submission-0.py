class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        ret = ""
        while i < len(word1) and i < len(word2):
            ret+=word1[i]
            ret+=word2[i]
            i+=1
        
        j = i
        while i < len(word1):
            ret+=word1[i]
            i+=1
        while j < len(word2):
            ret+=word2[j]
            j+=1
        
        return ret
