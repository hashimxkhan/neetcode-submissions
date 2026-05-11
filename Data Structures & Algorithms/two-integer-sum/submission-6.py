class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in count:
                return [count[num], i]
            count[nums[i]] = i

        



        

        