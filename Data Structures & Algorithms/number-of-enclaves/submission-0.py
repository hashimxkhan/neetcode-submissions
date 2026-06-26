class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        self.total = 0
        def dfs(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] != 1:
                return
            grid[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                    dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                self.total+= grid[i][j]
        return self.total