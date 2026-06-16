class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s)-1):
            cur = ord(s[i])
            nxt = ord(s[i+1])
            total+= abs(cur - nxt)
        return total
