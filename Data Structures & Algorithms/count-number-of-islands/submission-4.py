class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in dirs:
                    curR = row + dr
                    curC = col + dc
                    if curR in range(rows) and curC in range(cols) and grid[curR][curC] == "1" and (curR, curC) not in visited:
                        q.append((curR, curC))
                        visited.add((curR, curC))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
                    visited.add((r,c))
        return islands

