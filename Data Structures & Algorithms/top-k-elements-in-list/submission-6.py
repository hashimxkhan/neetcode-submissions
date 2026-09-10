class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        arr = []
        for key in freq:
            arr.append([-freq[key], key])
        
        ret = []
        heapq.heapify(arr)
        for i in range(k):
            num = heapq.heappop(arr)
            ret.append(num[1])
        return ret
            