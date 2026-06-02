class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(total):
            if total == target:
                return 1 
            if total > target:
                return 0
            
            count = 0
            if total in memo:
                return memo[total]
            for num in nums:
                count+= dp(num + total)
            memo[total] = count
            return memo[total]
        return dp(0)
        
            
