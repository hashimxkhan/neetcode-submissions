class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        prefix[0] = nums[0]
        rev = nums[::-1]
        postfix[0] = rev[0]
        for i in range(1,len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
            postfix[i] = rev[i] * postfix[i-1]
        postfix.reverse()
        
        ret = []
        ret.append(postfix[1])
        print(prefix)
        print(postfix)
        for i in range(1, len(nums)-1):
            ret.append(prefix[i-1] * postfix[i+1])
        ret.append(prefix[len(nums)-2])    
        return ret    

          
        


        