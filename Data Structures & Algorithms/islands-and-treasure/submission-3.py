class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi source check from all 0s to INF 
        inf = 2147483647
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        count = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] == inf:
                    grid[r][c] = count
                visited.add((r,c))
                dirs = [[1, 0], [-1, 0], [0,1], [0,-1]]
                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc
                    if (row in range(rows) and col in range(cols)
                    and (row,col) not in visited and grid[row][col] != -1):
                        q.append((row,col))
            count+=1

                
