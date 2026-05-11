class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        my_set = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        cur = [nums[i],nums[j], nums[k]]
                        cur.sort()
                        tup = tuple(cur)
                        if tup not in my_set:
                            ret.append([nums[i], nums[j],nums[k]])
                        my_set.add(tup)
        return ret

        