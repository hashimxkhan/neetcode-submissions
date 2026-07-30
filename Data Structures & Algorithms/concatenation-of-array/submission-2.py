class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.append(nums[i])
        for i in range(len(nums)):
            ret.append(nums[i])
        return ret