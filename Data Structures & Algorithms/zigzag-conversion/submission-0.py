class Solution:
    def convert(self, s: str, numRows: int) -> str:
        chars = {}
        for i in range(numRows):
            chars[i] = []
        cur = 0
        down = True
        for i in range(len(s)):
            chars[cur].append(s[i])
            if cur == numRows - 1:
                cur-=1
                down = False
            elif cur == 0:
                cur+=1
                down = True
            else:
                if down:
                    cur+=1
                else:
                    cur-=1
        print(chars)
        ret = ""

        for row in chars:
            arr = chars[row]
            for c in arr:
                ret+=c
        
        return ret
            