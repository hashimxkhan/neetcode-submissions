class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
                return
            board[r][c] = "A"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if r in [0,rows-1] or c in [0, cols-1]:
                    dfs(r,c)
        print(board)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "A":
                    board[r][c] = "O"


