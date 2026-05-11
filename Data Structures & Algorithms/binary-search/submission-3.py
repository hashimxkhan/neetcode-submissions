class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        flag = False
        while not flag and l <= h:
            mid = (h+l) // 2
            print(mid)
            if nums[mid] == target:
                 return mid
            elif nums[mid] > target:
                h = mid-1
            else:
                l = mid+1
        return -1
