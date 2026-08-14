class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        ret = ""
        flag = True
        while i < len(word1) or j < len(word2):
            if flag:
                if i >= len(word1):
                    ret = ret + word2[j]
                    j+=1
                    continue
                ret = ret + word1[i]
                i+=1
                flag = False
            else:
                if j >= len(word2):
                    ret = ret + word1[i]
                    i+=1
                    continue
                ret = ret + word2[j]
                j+=1
                flag = True
        return ret