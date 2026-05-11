class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ret = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        sorted_count = sorted(count.items(), key= lambda x:x[1], reverse= True)
        for key,v in sorted_count:
            ret.append(key)
            k-=1
            if k == 0:
                return ret

