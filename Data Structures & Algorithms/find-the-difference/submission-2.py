class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen1 = {}
        seen2 = {}
        for c in s:
            if c not in seen1:
                seen1[c] = 0
            seen1[c]+=1
        for c in t:
            if c not in seen2:
                seen2[c] = 0
            seen2[c]+=1
        for c in seen2:
            while seen2[c] > 0:
                if c not in seen1 or seen1[c] == 0:
                    return c
                seen1[c]-=1
                seen2[c]-=1
