class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # O(n) with division
        product = 1
        zeroCount = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeroCount+=1
                index = i
            else:
                product = num * product
        if zeroCount > 1:
            return [0] * len(nums)

        if zeroCount == 1:
            arr = [0] * len(nums)
            arr[index] = product
            return arr

        ret = [] 
        for num in nums:
            ret.append(product//num)
        return ret


        