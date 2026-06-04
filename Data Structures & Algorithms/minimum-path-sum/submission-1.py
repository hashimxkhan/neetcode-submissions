class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cache = {}

        def dp(i,j):
            if i >= rows or j >= cols:
                return float('inf')
            
            if i == rows-1 and j == cols-1:
                return grid[i][j]
            
            if (i,j) in cache:
                return cache[(i,j)]

            cache[(i,j)] = grid[i][j] + min(dp(i+1,j), dp(i,j+1))
            return cache[(i,j)]
        
        return dp(0,0)
            
