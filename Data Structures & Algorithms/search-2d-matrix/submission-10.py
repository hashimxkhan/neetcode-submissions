class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first = 0
        last = len(matrix) - 1
        row = -1
        while first <= last:
            cur = (first + last) // 2
            if matrix[cur][0] > target:
                last = cur-1
            elif matrix[cur][len(matrix[0])-1] < target:
                first = cur+1
            else:
                row = cur
                break
        if row == -1:
            return False
        

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = (l+r) // 2
            print(m)
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m-1
            else:
                l = m+1
        return False