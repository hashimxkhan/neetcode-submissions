class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapsort(heap):
            ret = []
            while heap:
                ret.append(heapq.heappop(heap))
            return ret
        

        heapq.heapify(nums)
        return heapsort(nums)
        