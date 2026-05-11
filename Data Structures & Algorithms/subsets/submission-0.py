class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        def dfs(i):
            # base case
            if i == len(nums):
                res.append(sol.copy())
                return
            
            # Make decision
            # dont add i
            dfs(i+1)

            # add i
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
        dfs(0)
        return res
        