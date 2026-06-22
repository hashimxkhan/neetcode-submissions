class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # brute force
        best = 0
        
        for i in range(len(fruits)):
            num = 0
            types = set()
            for j in range(i, len(fruits)):
                types.add(fruits[j])
                if len(types) > 2:
                    break
                best = max(best, j - i + 1)
        return best


