class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        ret = []
        while nums:
            ret.append(heapq.heappop(nums))
        return ret