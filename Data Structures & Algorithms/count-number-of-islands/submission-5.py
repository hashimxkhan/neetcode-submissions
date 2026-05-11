class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c] == "0":
                return
            # it means its a new island or part of an existing island
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    res+=1
                    dfs(r,c)
                 #   visited.add((r,c))
        return res
    