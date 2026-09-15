class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def can(i):
            if i >= len(nums) - 1:
                return True
            if i in cache:
                return cache[i]
            if nums[i] == 0:
                return False
            
            for j in range(1, nums[i]+1):
                nxt = i + j
                if can(nxt):
                    cache[i] = True
                    return cache[i]
            cache[i] = False
            return cache[i]
    
        return can(0)