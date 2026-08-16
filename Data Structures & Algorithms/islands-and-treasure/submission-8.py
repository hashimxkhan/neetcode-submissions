class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        seen = set()
        def bfs():
            dist = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()     
                    grid[row][col] = dist
                    dirs = [[1,0], [-1,0], [0,1], [0,-1]]
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == -1 or (nr,nc) in seen:
                            continue
                        seen.add((nr,nc))
                        q.append((nr,nc))
                dist+=1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    seen.add((i,j))
                    q.append((i,j))   
        bfs()      
