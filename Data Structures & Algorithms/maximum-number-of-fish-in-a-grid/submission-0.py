class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j, seen):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in seen or grid[i][j] == 0:
                return 0
            
            seen.add((i,j))
            return (grid[i][j] + dfs(i+1, j, seen) + dfs(i-1,j, seen) + dfs(i,j+1, seen) + dfs(i, j-1, seen))
        
        best = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    best = max(best, dfs(i, j, set()))
        return best
