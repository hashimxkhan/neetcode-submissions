class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        maps = {}
        for i in range(len(order)):
            maps[order[i]] = i
        
        def comparison(a):
            ret = []
            for c in a:
                ret.append(maps[c])
            return ret
                
        
        return words == sorted(words, key=comparison)

