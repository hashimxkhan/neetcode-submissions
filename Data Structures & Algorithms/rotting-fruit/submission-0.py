class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        time = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append([r,c])
                        fresh-=1
            time+=1
        return time if fresh == 0 else -1                



        
        