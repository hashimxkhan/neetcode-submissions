class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r, c-1)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    best = max(best, dfs(i,j))

        return best 
            