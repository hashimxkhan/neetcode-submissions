class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = []
        cur = 0
        for word in words:
            if word[0] in "aeiou" and word[len(word)-1] in "aeiou":
                cur+=1
            prefix.append(cur)
        print(prefix)

        ret = []
        for q in queries:
            cur = 0
            l,r = q
            cur = prefix[r] - prefix[l]
            if words[l][0] in "aeiou" and words[l][len(words[l])-1] in "aeiou":
                cur+=1
            ret.append(cur)
        return ret

