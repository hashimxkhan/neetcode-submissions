class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ret = 0
        for word in words:
            flag = True
            for c in word:
                if c not in allowed:
                    flag = False
            if flag:
                ret+=1
        return ret 
            
        