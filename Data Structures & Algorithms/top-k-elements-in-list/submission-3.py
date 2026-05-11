class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        sortedFreq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

        ret = []
        for key in sortedFreq:
            if k == 0:
                break
            ret.append(key[0])
            k-=1
        return ret
        