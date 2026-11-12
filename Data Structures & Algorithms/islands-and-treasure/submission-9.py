class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or (i, j) in seen or grid[i][j] == -1:
                return float('inf')

            if grid[i][j] == 0:
                return 0
            
            seen.add((i,j))
            return 1 + min(dfs(i,j+1), dfs(i, j-1), dfs(i+1,j), dfs(i-1,j))
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2147483647:
                    seen = set()
                    grid[i][j] = dfs(i,j)
