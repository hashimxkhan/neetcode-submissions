class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        heap = []
        ret = []
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        for key, value in hashMap.items():
            heap.append((-value, key))
        heapq.heapify(heap)
        for i in range(k):
            value, key = heapq.heappop(heap)
            ret.append(key)
        return ret


        


            
            

        