class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToInd = {}
        for ind, val in enumerate(nums):
            num = target - val
            if num in valToInd:
                return [valToInd[num], ind]
            valToInd[val] = ind
