class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def dist(x,y):
            return ((x ** 2) + (y ** 2)) ** 0.5
        for point in points: # n
            x, y = point
            distance = dist(x,y)
            heap.append([distance, x, y])
        
        ret = []
        heapq.heapify(heap)
        i = 0
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            ret.append([x,y])
            k-=1
        return ret

