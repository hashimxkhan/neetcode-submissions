class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        prev = 0
        for c in s:
            if c == ' ':
                if count > 0:
                    prev = count
                count = 0
            else:
                count+=1
        if s[len(s)-1] == ' ':
            return prev
        return count