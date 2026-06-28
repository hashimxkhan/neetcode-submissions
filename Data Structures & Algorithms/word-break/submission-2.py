class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    if dp(i+ len(word)):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]
        return dp(0)
            

            
            