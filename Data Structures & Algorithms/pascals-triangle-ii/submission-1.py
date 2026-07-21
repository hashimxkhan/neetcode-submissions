class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [0] + [1] + [0]
        for i in range(1, rowIndex+1):
            new = []
            for j in range(i+1):
                new.append(cur[j] + cur[j+1])
            new = [0] + new + [0]
            cur = new
        return cur[1:-1]