class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        count = 0
        cur = 0
        while r < len(chars):
            if chars[r] == chars[l]:
                count+=1
            else:
                if count <= 1:
                    chars[cur] = chars[l]
                    l = r
                    cur+=1
                else:
                    strCount = str(count)
                    chars[cur] = chars[l]
                    cur+=1
                    for s in strCount:
                        chars[cur] = s
                        cur+=1
                    l = r
                count = 1
            r+=1
        if count > 0:
            chars[cur] = chars[l]
            cur+=1
            if count > 1:
                strCount = str(count)
                for s in strCount:
                    chars[cur] = s
                    cur+=1
        return cur

