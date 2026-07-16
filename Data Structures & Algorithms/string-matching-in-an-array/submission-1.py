class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    ret.append(words[i])
                    break
        return ret