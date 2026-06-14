class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = [ 0 for _ in range(len(arr))]
        cur = -1
        for i in range(len(arr)-1, -1, -1):
            right[i] = cur
            if cur <= arr[i]:
                cur = arr[i]
        return right

