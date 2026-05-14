class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        hash = {}
        quads = set()
        for i in range(len(nums)):
            hash[nums[i]] = i
        
        ret = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    val = (nums[i] + nums[j] + nums[k] - target) * -1
                    if val in hash:
                        if hash[val] == i or hash[val] == j or hash[val] == k:
                            continue
                        arr = [nums[i],nums[j], nums[k], val]
                        arr.sort()
                        tup = tuple(arr)
                        if tup in quads:
                            continue
                        quads.add(tup )
                        ret.append(arr)
        return ret
