class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def check(r,c):
            row = False
            column = False
            for i in range(len(grid[0])):
                if i != c and grid[r][i] == 1:
                    row = True
            for i in range(len(grid)):
                if r != i and grid[i][c] == 1:
                    column = True
            return row or column


        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if check(i,j):
                        ret+=1
        return ret
                
            
