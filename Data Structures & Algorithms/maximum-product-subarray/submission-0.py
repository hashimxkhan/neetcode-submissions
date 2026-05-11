class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = float('-inf')

        for i in range(len(nums)):
            curProduct = nums[i]
            for j in range(i, len(nums)):
                if i != j:
                    curProduct = curProduct * nums[j]
                product = max(curProduct, product)
        return product