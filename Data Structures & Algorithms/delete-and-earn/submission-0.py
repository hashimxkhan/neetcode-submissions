class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        best = 0
        maps = {}
        for num in nums:
            if num not in maps:
                maps[num] = 0
            maps[num]+=1
        
        total = sum(nums)

        for num in maps:
            cur = total

            if num + 1 in maps:
                cur -= (maps[num+1] * num+1)
            
            if num-1 in maps:
                cur-= (maps[num-1] * num-1)
            best = max(best, cur)
        
        return best

