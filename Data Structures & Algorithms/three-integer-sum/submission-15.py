class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        maps = {}
        for i in range(len(nums)):
            if nums[i] not in maps:
                maps[nums[i]] = []
            maps[nums[i]].append(i)
        
        seen = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                third = (nums[i] + nums[j]) * -1
                if third in maps:
                    for k in maps[third]:
                        if k != i and k != j:
                            arr = [nums[i], nums[j],third]
                            arr.sort()
                            seen.add(tuple(arr))
                            break
        ret = []
        for ans in seen:
            i,j,k = ans
            ret.append([i,j,k])
        return ret

