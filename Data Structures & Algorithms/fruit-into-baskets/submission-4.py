class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        best = 0
        for i in range(len(fruits)):
            cur = 0
            seen = set()
            for j in range(i, len(fruits)):
                seen.add(fruits[j])
                if len(seen) > 2:
                    break
                cur = j - i + 1
                best = max(best, cur)
        return best


