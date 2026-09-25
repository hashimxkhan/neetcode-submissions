class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        l = 0
        r = 0
        while r < k:
            heapq.heappush(heap, (-nums[r], r))
            r+=1
        ret = []
        while r <= len(nums):
            while True:
                cur = heapq.heappop(heap)
                if cur[1] >= l:
                    ret.append(-cur[0])
                    heapq.heappush(heap, cur)
                    break
            if r == len(nums):
                break
            heapq.heappush(heap, (-nums[r], r))
            l+=1
            r+=1
        return ret

