class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        def dfs(r,c):
            if r < 0 or c < 0 or c >= len(grid[0]) or r >= len(grid) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return ( 1 + dfs(r+1,c) +
            dfs(r-1,c) + 
            dfs(r,c+1) +
            dfs(r,c-1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res


        