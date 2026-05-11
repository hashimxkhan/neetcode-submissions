class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = nums[i]
            if target > 0: # all positives cannot be = 0
                break
            l = i+1
            h = len(nums)-1
            while l < h:
                threeSum = target + nums[l] + nums[h]
                if threeSum > 0:
                    h-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([target, nums[l], nums[h]])
                    l+=1
                    h-=1
                    while nums[l-1] == nums[l] and l < h:
                        l+=1
        return res





        