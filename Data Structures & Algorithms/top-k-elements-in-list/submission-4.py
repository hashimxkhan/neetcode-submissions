class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums: # n
            freq[num] = 1 + freq.get(num, 0)
        
        heap = []
        for key in freq: # n
            heap.append([-freq[key], key])

        heapq.heapify(heap) # n

        ret = []
        while k > 0:
            frequency, num = heapq.heappop(heap)
            ret.append(num)
            k-=1
        return ret
            

