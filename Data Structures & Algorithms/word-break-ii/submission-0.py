class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sets = set(wordDict)
        ret = []
        def dp(i, string, prev):
            if i == len(s):
                if s[prev:i] in sets:
                    ret.append(string)
                return
            if i > len(s):
                return
            
            if s[prev:i+1] in sets:
                new = string + s[i] + ' '
                dp(i+1, string + s[i], prev)
                dp(i+1, new, i+1)
            else:
                string+= s[i]
                dp(i+1, string, prev)
        dp(0, "", 0)
        return ret



