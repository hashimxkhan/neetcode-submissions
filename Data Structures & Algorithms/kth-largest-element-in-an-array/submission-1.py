class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = []
        for num in nums:
            neg.append(-num)
        heapq.heapify(neg) #n
        while k > 1: 
            heapq.heappop(neg)
            k-=1
        return -neg[0]
