class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        zeroProduct = nums[0]
        count = 0
        for i in range(1, len(nums)):
            product = product * nums[i]
            if nums[i] == 0:
                count+=1
                continue
            zeroProduct = zeroProduct * nums[i]
            
        ret = []
        if count > 1:
            for i in range(len(nums)):
                ret.append(0)
            return ret
        for n in nums:
            if n == 0:
                ret.append(zeroProduct)
            else:
                ret.append(int(product / n))
        return ret


        