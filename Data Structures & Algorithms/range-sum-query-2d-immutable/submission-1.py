class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix.copy()
        self.rows = [[0 for _ in range(len(self.matrix))] for _ in range(len(self.matrix[0]))]
        for i in range(len(self.matrix[0])):
            cur = 0
            for j in range(len(self.matrix)):
                cur+= self.matrix[j][i]
                self.rows[i][j] = cur

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(col1, col2+1):
            val = 0
            if row1 > 0:
                val = self.rows[i][row1 - 1]
            print(val)

            
            colSum = self.rows[i][row2] - val
            total+=colSum
        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)