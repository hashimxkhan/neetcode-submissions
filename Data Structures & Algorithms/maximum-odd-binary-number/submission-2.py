class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = -1
        for i in range(len(s)):
            if s[i] == "1":
                count+=1
        
        
        ret = ""
        for i in range(len(s)):
            if i == len(s) - 1:
                ret+="1"
                return ret
            if count > 0:
                ret+="1"
                count-=1
            else:
                ret+="0"
                
