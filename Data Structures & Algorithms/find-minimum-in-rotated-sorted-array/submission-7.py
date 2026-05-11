class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        ans = nums[0]
        while l <= h:
            m = (l+h) // 2
            if nums[l] < nums[h]:
                ans = min(ans, nums[l])
                break
            ans = min(ans, nums[m])
            if nums[l] <= nums[m]:
                print(nums[l], nums[m])
                ans = min(nums[l], ans)
                l = m+1
            else:
                ans = min(nums[m], ans)
                h = m-1
        return ans
        

        