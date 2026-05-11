class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0), (0,1), (0,-1)]
        q = deque()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]  == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist

                for dr, dc in dirs:
                    row = i + dr
                    col = j + dc
                    if (row >= 0 and row < rows and col >= 0 and col < cols
                        and grid[row][col] != -1 and (row,col) not in visited):
                        q.append((row,col))
                        visited.add((row,col))
            dist+=1
