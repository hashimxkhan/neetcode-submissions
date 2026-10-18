class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        cache = {}
        def dp(i, j):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return 0
            if matrix[i][j] == "0":
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)] = 1 + min(dp(i, j-1), dp(i-1, j-1), dp(i-1, j))
            return cache[(i,j)]

        best = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                best = max(best, dp(i,j))
                print (i, j, best)
        return best * best
        
