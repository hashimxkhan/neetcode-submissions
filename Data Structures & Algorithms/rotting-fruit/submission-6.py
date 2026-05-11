class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        fresh = 0
        q = deque()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        
        mins = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc
                    if (row >= 0 and row < rows and col >= 0 and col < cols and
                        (row,col) not in visited and grid[row][col] != 0):
                        fresh-=1
                        grid[row][col] = 2
                        q.append((row,col))
                        visited.add((row,col))
            mins+=1

        if fresh > 0:
            return -1
        else:
            return mins