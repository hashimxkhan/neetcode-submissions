class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        hashMap = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s not in hashMap:
                hashMap[s] = []
            hashMap[s].append(i)
        for key in hashMap:
            print(key)
            curList = []
            for ind in hashMap[key]:
                curList.append(strs[ind])
            ret.append(curList)
        return ret
            
        


            


