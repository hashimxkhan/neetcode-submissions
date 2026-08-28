class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        seen = set()
        for i in range(len(nums)):
            r = len(nums) - 1
            l = 0
            while l <= r:
                if l == i:
                    l+=1
                    continue
                if r == i:
                    r-=1
                    continue
                
                score = nums[l] + nums[i] + nums[r]
                if score > 0:
                    r-=1
                elif score < 0:
                    l+=1
                else:
                    arr = [nums[i],nums[l],nums[r]]
                    arr.sort()
                    if tuple(arr) not in seen and l != r:
                        seen.add(tuple(arr))
                        ret.append(arr)
                    l+=1
                    r-=1
        return ret
