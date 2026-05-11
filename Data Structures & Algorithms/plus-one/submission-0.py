class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for d in digits:
            s = s + str(d)
        s = str(int(s) + 1)
        ret = []
        for c in s:
            ret.append(int(c))
        return ret
            
        