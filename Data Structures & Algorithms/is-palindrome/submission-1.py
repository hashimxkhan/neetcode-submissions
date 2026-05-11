class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', "", s)
        l = 0
        h = len(s) - 1
        s = s.lower()
        while l < h:
            if s[l] != s[h]:
                return False
            h-=1
            l+=1
        return True

        