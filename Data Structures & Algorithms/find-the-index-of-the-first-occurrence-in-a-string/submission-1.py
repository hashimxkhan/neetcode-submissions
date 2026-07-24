class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            j = 0
            cur = 0
            while j < len(needle) and (i+j) < len(haystack) and needle[j] == haystack[i+j]:
                cur+=1
                j+=1
            if cur == len(needle):
                return i
        return -1