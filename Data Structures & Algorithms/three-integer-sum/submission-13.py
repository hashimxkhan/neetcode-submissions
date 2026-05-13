class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash = {}
        triplets = set()
        nums.sort()
        for i in range(len(nums)):
            hash[nums[i]] = i
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                third = (nums[i] + nums[j]) * -1
                if third in hash:
                    if hash[third] == i or hash[third] == j or i == j:
                        continue
                    triple = [nums[i],nums[j], third]
                    triple.sort()
                    tup = tuple(triple)
                    if tup not in triplets:
                        triplets.add(tup)
        

        ret = []
        for triple in triplets:
            i,j,k = triple
            arr = [i,j,k]
            ret.append(arr)
        return ret

