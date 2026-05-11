class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][n-1] == target:
                return True
            elif matrix[i][n-1] > target:
                row = i
                break
        return self.binarySearch(matrix, target, row)

    def binarySearch(self, matrix: List[List[int]], target: int, row: int ) -> bool:
        l = 0
        h = len(matrix[0])-1
        while l <= h:
            print(l,h)
            mid = (h + l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                h=mid-1
            else:
                l=mid+1
        return False

