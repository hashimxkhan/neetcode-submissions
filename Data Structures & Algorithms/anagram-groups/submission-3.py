class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            cur = [0] * 26
            for c in s:
                cur[ord(c) - ord("a")]+=1
            if tuple(cur) not in res:
                res[tuple(cur)] = []
            res[tuple(cur)].append(s)


        ret = []
        for key in res:
            ret.append(res[key])
        return ret