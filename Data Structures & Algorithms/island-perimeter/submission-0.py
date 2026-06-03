class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        self.count = 0
        def dfs(i,j):
            if i >= rows or j >= cols:
                return 0
            if grid[i][j] == 0:
                return 0
            
            
            cur = 0
            if i+1 >= rows or grid[i+1][j] == 0:
                cur+=1
            if i-1 < 0 or grid[i-1][j] == 0:
                cur+=1
            if j+1 >= cols or grid[i][j+1] == 0:
                cur+=1
            if j-1 < 0 or grid[i][j-1] == 0:
                cur+=1
            
            self.count+= cur
            return cur
        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j)
        return self.count