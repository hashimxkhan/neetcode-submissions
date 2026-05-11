class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc
                    if (row in range(rows) and
                    col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh-=1
                        q.append((row,col))
            time+=1
        if fresh > 0:
            return -1
        return time

                    





