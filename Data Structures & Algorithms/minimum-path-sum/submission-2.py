class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        cache = {}
        def dp(r, c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return float('inf')
            if (r,c) in cache:
                return cache[(r,c)]
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return grid[len(grid) - 1][len(grid[0]) - 1]
            
            cache[(r,c)] = grid[r][c] + min(dp(r+1,c), dp(r, c+1))
            return cache[(r,c)]
        
        return dp(0,0)