class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        while l <= h:
            m = (l+h) // 2
            if nums[m] == target:
                return m
            # left sorted
            if nums[l] <= nums[m]:
                if nums[m] < target or nums[l] > target:
                    l = m+1
                else:
                    h = m-1
            # right sorted
            else:
                if nums[m] > target or target > nums[h]:
                    h = m-1
                else:
                    l = m+1
        return -1
                    

            


        
        

        