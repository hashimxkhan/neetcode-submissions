class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarysearch(arr):
            l = 0
            r = len(arr)
            print(arr)
            while l <= r:
                m = (r+l) // 2
                if arr[m] == target:
                    return True
                elif arr[m] > target:
                    r = m-1
                else:
                    l = m+1
            return False
        
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (r+l) // 2
            if matrix[m][0] <= target and matrix[m][len(matrix[0])-1] >= target:
                return binarysearch(matrix[m])
            elif matrix[m][0] > target:
                r = m-1
            else:
                l = m+1
        return False