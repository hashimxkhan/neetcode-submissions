class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maps = {}
        for c in s:
            if c not in maps:
                maps[c] = 0
            maps[c]+=1
        
        ret = []
        cur = 0
        sets = set()
        for i in range(len(s)):
            sets.add(s[i])
            maps[s[i]]-=1
            flag = True
            for num in sets:
                if maps[num] > 0:
                    flag = False
                    break
            if flag:
                ret.append(i - cur + 1)
                sets = set()
                cur = i+1
            

        return ret