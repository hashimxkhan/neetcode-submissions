class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if  n == 1:
            return nums[0]
        cache1 = [-1] * n
        cache2 = [-1] * n
        def maxMoney(i, ind):
            if i >= n:
                return 0
            if i == n-1:
                if ind == 1:
                    return nums[i]
                else:
                    return 0
            if ind == 1:
                if cache1[i] != -1:
                    return cache1[i]
                cache1[i] = max(maxMoney(i+1, ind), nums[i] + maxMoney(i+2, ind))
                return cache1[i]
            else:
                if cache2[i] != -1: 
                    return cache2[i]
                cache2[i] = max(maxMoney(i+1, ind), nums[i] + maxMoney(i+2, ind))
                return cache2[i]
        return max(maxMoney(0,0), maxMoney(1,1))

