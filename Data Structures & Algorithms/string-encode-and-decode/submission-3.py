class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            
            l = ""
            while s[i] != "#":
                l+= s[i]
                i+=1
            i+=1
            length = int(l)
            cur = ""
            for j in range(length):
                cur+= s[i]
                i+=1
            res.append(cur)

        return res
