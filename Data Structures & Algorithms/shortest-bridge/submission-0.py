class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        

        seen = set()
        q = deque()
        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in seen or grid[r][c] == 0:
                return
            seen.add((r,c))
            q.append((r,c))
            grid[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        

            
        def bfs():
            ct = -1
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    if grid[r][c] == 1:
                        return ct
                    dirs = [[1,0], [-1,0], [0,-1], [0,1]]
                    for dr,dc in dirs:
                        nr = r + dr
                        nc = c + dc
                        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or (nr,nc) in seen:
                            continue
                        else:
                            seen.add((nr,nc))
                            q.append((nr,nc))
                ct+=1
            return ct




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return bfs()