class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        cur = ''
        words = []
        for c in s:
            if c == ' ':
                words.append(cur)
                cur = ''
            else:
                cur+=c
        words.append(cur)
        seen1 = set()
        seen2 = set()
        for word in words:
            seen1.add(word)
        for c in pattern:
            seen2.add(c)
        return len(pattern) == len(words) and len(seen1) == len(seen2)