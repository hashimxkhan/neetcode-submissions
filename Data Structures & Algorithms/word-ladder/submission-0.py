class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        res = 0
        q = deque([beginWord])

        while q:
            res+=1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for i in range(len(cur)):
                    for c in range(97,123):
                        if chr(c) == cur[i]:
                            continue
                        nxt = cur[:i] + chr(c) + cur[i+1:]
                        if nxt in words:
                            q.append(nxt)
                            words.remove(nxt)
        return 0