class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        ret = []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for num in freq:
            if freq[num] > (len(nums) // 3):
                ret.append(num)
        
        return ret