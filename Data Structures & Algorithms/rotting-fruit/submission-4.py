class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(r,c):
            dist = 0
            q = deque()
            visited = set()
            q.append((r,c))
            visited.add((r,c))
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()

                    if grid[r][c] == 2:
                        return dist
                    
                    for dr, dc in dirs:
                        row = r + dr
                        col = c + dc
                        if (row >= 0 and row < rows and col >= 0 and col < cols
                            and (row,col) not in visited and grid[row][col] != 0):
                            q.append((row,col))
                            visited.add((row,col))
                dist+=1
            return -1
        
        maxMins = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    mins = bfs(i,j)
                    if mins == -1:
                        return -1
                    maxMins = max(mins, maxMins)
        return maxMins
                    
