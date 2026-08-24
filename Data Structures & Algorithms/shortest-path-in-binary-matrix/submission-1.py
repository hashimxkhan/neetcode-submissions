class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        
        dirs = [[1,0], [-1,0], [0,-1], [0,1], [1,1], [1,-1], [-1,1], [-1,-1]]
        q = deque()
        seen = set()
        q.append((0,0))
        seen.add((0,0))
        count = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == rows-1 and c == cols-1:
                    return count
                
                for dr,dc in dirs:
                    nr,nc = r + dr, c + dc
                    if not (nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr,nc) in seen or grid[nr][nc] == 1):
                        q.append((nr,nc))
                        seen.add((nr,nc))
            count+=1
        return -1


                
                
