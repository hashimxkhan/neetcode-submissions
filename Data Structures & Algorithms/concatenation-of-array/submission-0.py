class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ret = nums.copy()

        for num in nums:
            ret.append(num)
        
        return ret
        