class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set = set()
        for c in nums:
            if c in my_set:
                return c
            my_set.add(c)
        

        