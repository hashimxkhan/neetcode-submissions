class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        l,r = 0,0
        ret = []
        while r < len(nums):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)
            if d[0] < l:
                d.popleft()
            if r + 1 >= k:
                ret.append(nums[d[0]])
                l+=1
            r+=1
        return ret
                
