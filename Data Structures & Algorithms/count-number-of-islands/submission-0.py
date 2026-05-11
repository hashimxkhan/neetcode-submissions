class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        numIslands  = 0
        
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [-1, 0], [0,1], [0,-1]]
                for dr, dc in dirs:
                    r = row+dr
                    c = col + dc
                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == "1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and ((r,c)) not in visited:
                    bfs(r,c)
                    numIslands+=1
                    visited.add((r,c))
        return numIslands

            
                        


