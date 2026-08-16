class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][len(matrix[0])-1] >= target:
                for j in range(len(matrix[0])):
                    cur = matrix[i][j]
                    if cur == target:
                        return True
        return False