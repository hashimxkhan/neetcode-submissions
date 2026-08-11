class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first = words[0]
        maps = {}
        for c in first:
            if c not in maps:
                maps[c] = 0
            maps[c]+=1
        
        for i in range(1, len(words)):
            cur = {}
            word = words[i]
            for c in word:
                if c not in cur:
                    cur[c] = 0
                cur[c]+=1
            
            for key in maps:
                if key not in cur:
                    maps[key] = 0
                else:
                    maps[key] = min(maps[key], cur[key])
            
        ret = []
        print(maps)
        for key in maps:
            for i in range(maps[key]):
                ret.append(key)
        return ret

