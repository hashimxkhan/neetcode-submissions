class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        cur = s[0]
        for i in range(1, len(s)):
            score += abs(ord(cur) - ord(s[i]))
            cur = s[i]
        return score
