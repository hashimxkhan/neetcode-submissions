class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return True
            if grid[r][c] == 0 or (r,c) in seen:
                return False
            
            seen.add((r,c))
            return dfs(r+1,c) or dfs(r-1,c) or dfs(r,c+1) or dfs(r,c-1)




        num = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    seen = set()
                    if not dfs(i,j):
                        num+=1
        return num
                    