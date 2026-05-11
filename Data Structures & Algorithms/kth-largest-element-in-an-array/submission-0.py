class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        i = len(nums) - k
        while i > 0:
            heapq.heappop(nums)
            i-=1
        return nums[0]
