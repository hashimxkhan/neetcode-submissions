class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_set = set()
        for row in board:
            for index in row:
                if index == ".": continue
                if index in my_set:
                    return False
                my_set.add(index)
            my_set.clear()

        for i in range(8):
            for j in range(8):
                if board[j][i] == ".": continue
                if board[j][i] in my_set:
                    return False
                my_set.add(board[j][i])
            my_set.clear()

        for k in range(9):
            for i in range(3):
                for j in range(3):
                    row = (k//3) * 3 + i
                    col = (k % 3) * 3 + j
                    if board[row][col] == ".": continue
                    if board[row][col] in my_set:
                        return False
                    my_set.add(board[row][col])
            my_set.clear()

        return True



        





        