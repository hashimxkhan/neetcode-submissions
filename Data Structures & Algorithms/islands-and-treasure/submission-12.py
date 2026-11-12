class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        ct = 0
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in seen or grid[i][j] == -1:
                    continue
                seen.add((i,j))
                if grid[i][j] > 0:
                    grid[i][j] = min(grid[i][j], ct)
                
                q.append((i+1, j))
                q.append((i-1, j))
                q.append((i,j+1))
                q.append((i,j-1))
            ct+=1
        
                