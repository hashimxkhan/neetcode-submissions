class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        ret = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                product = product * nums[j]
            ret.append(product)
        return ret
        