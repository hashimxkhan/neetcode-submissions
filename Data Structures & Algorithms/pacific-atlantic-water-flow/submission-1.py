class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        res = []

        def bfs(r,c):
            q = collections.deque()
            visited = set()
            q.append((r,c))
            visited.add((r,c))
            atlantic = False
            pacific = False
            dirs = [[1,0], [-1,0],[0,1],[0,-1]]
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    if r == 0 or c == 0:
                        pacific = True
                    if r == rows-1 or c == cols-1:
                        atlantic = True
                    for dr,dc in dirs:
                        row = r + dr
                        col = c + dc
                        if row in range(rows) and col in range(cols) and heights[r][c] >= heights[row][col] and (row,col) not in visited:
                            q.append((row,col))
                            visited.add((row,col))
            return atlantic and pacific



        for r in range(rows):
            for c in range(cols):
                ans = bfs(r,c)
                if ans:
                    res.append([r,c])
        return res