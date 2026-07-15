class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for i in range(len(s)):
            if s[i] == '1':
                count+=1
        
        length = len(s)
        ret  = ""
        while count > 1:
            ret = ret + '1'
            count-=1
        
        diff = length - len(ret)
        for i in range(diff-1):
            ret = ret + '0'
        
        ret = ret + '1'
        return ret