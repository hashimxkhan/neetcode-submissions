class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = {}
        if len(s1) > len(s2):
            return False
        for i, c in enumerate(s1):
                first[c] = first.get(c,0) + 1
        l = 0
        r = len(s1) - 1
        second = {}
        for i in range(l,r+1):
            second[s2[i]] = second.get(s2[i],0) + 1
        while r < len(s2):
            flag = True
            for i in range(l, r+1):
                char = s2[i]
                firstFreq = first.get(char, 0)
                secondFreq = second[char]
                if firstFreq != secondFreq:
                    print(second)
                    print(first)
                    flag = False
            if flag:
                return True
            second[s2[l]] = second.get(s2[l]) - 1
            l+=1
            r+=1
            if r == len(s2):
                break
            second[s2[r]] = second.get(s2[r], 0) + 1
        return False






        
        
            

        