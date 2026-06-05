class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def dp(i,j):
            if i >= rows or j >= cols or j < 0 or i < 0:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
        
            up, down, right, left = 0,0,0,0
            if i+1 < rows and matrix[i+1][j] > matrix[i][j]:
                down = 1 + dp(i+1,j)
            
            if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                up = 1 + dp(i-1, j)
            
            if j+1 < cols and matrix[i][j+1] > matrix[i][j]:
                right = 1 + dp(i,j+1)
            
            if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                left = 1 + dp(i, j-1)
            
            cache[(i,j)] = max(1,up, down, right, left)
            return cache[(i,j)]
        
        best = 0
        for i in range(rows):
            for j in range(cols):
                best = max(best, dp(i,j))
        return best

