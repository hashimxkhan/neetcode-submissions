class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ret = []
        for q in queries:
            l, r = q
            cur = 0
            for i in range(l, r + 1):
                word = words[i]
                if word[0] in "aeiou" and word[len(word) - 1] in "aeiou":
                    cur+=1
            ret.append(cur)
        return ret