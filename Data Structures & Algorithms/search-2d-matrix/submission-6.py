class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <=r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][len(matrix[0]) - 1] < target:
                l = m + 1
            else:
                a = 0
                b = len(matrix[0]) - 1
                while a <= b:
                    mid = (a+b) // 2
                    if matrix[m][mid] == target:
                        return True
                    elif matrix[m][mid] > target:
                        b = mid-1
                    else:
                        a = mid+1
                break
        return False
