class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = set()
        r = 0
        ret = []
        while r + k <= len(nums):
            for i in range(k):
                window.add(nums[r+i])
            ret.append(max(window))
            r+=1
            window = set()
        return ret





