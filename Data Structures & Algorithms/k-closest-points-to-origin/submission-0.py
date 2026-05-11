class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def dist(x,y):
            return ((x ** 2) + (y ** 2)) ** 0.5
        for point in points:
            x, y = point
            distance = dist(x,y)
            heap.append([distance, x, y])
        
        ret = []
        heap.sort(key=lambda x:x[0]) # sort on first key
        i = 0
        while i < k and i < len(heap):
            dist, x, y = heap[i]
            ret.append([x,y])
            i+=1
        return ret

