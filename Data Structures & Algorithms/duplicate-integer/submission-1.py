class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for num in nums:
            if num in dups:
                return True
            else:
                dups[num] = num
        return False
       
         