class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash = {}
        for a in arr:
            if a not in hash:
                hash[a] = 0
            hash[a]+=1
        
        best = -1
        for key in hash:
            if key == hash[key]:
                best = max(best, key)
        return best