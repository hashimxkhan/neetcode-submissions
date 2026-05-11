class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        ret = []
        for num in nums:
            if num in frequency:
                frequency[num]+=1
            else:
                frequency[num] = 1
        for key in sorted(frequency, key = lambda k: frequency[k], reverse = True):
            ret.append(key)
        return ret[:k]

        


            
            

        