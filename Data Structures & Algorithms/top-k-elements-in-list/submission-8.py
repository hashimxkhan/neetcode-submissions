class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for num in nums:
            if num not in maps:
                maps[num] = 0
            maps[num]+=1
        
        heap = []
        for key in maps:
            heap.append([-maps[key], key])
        heapq.heapify(heap) # O(N)

        # should check if len heap < k btw
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


