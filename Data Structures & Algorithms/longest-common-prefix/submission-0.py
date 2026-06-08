class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        c = len(pre)
        for stri in strs:
            cur = 0
            for j in range(c):
                if j < len(stri) and stri[j] == pre[j]:
                    cur+=1
                else:
                    break
            c = min(cur, c)
        
        return pre[:c]
