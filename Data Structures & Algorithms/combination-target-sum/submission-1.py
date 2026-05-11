class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        def dfs(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return
            if i == len(nums) or total > target: # leaf stop recursing
                return
            # make decision to choose cur
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, sol, 0)
        return res
        