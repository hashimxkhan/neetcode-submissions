class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heap.append(-gift)
        heapq.heapify(heap)
        for i in range(k):
            biggest = heapq.heappop(heap) * -1
            root = int(sqrt(biggest))
            heapq.heappush(heap, -root)
        
        total  = 0
        while heap:
            total += heapq.heappop(heap)
        return total * -1