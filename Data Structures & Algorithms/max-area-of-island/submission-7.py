class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]
        def bfs(r,c):
            q = []
            q.append((r,c))
            count = 0
            grid[r][c] = 0
            while q:
                count+=1
                row, col = q.pop()
                grid[row][col] = 0
                for dr, dc in dirs:
                    nr, nc = row+dr, col + dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return count
        
        best = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    best = max(best, bfs(i,j))
        return best