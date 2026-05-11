class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return grid
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        visited = set()
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        dist = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                curR, curC = q.popleft()
                if grid[curR][curC] == INF:
                    grid[curR][curC] = dist
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in dirs:
                    row = curR + dr
                    col = curC + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] != -1 and (row,col) not in visited:
                        q.append((row,col))
                        visited.add((row, col))                            
            dist+=1
