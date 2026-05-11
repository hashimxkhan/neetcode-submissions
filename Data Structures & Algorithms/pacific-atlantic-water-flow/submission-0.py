class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        res = []
        def bfs(r,c):
            pacific = False
            atlantic = False
            visited = set()
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                if row == rows-1 or col == cols-1:
                    atlantic = True
                if row == 0 or col == 0:
                    pacific = True
                for dr, dc in dirs:
                    curR = row + dr
                    curC = col + dc
                    if curR in range(rows) and curC in range(cols) and heights[curR][curC] <= heights[row][col] and (curR, curC) not in visited:
                        q.append((curR, curC))
                        visited.add((curR, curC))
            return pacific and atlantic

        for r in range(rows):
            for c in range(cols):
                ans = bfs(r,c)
                if ans:
                    res.append([r,c])
        return res
