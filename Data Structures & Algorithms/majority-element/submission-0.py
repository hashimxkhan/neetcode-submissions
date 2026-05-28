class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = {}

        for num in nums:
            if num not in maps:
                maps[num] = 0
            maps[num]+= 1
            if maps[num] > len(nums) // 2:
                return num