class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i, total):
            if total > target or i == len(nums):
                return
            if total == target:
                res.append(cur.copy())
                return
            # make decison
            # choose
            cur.append(nums[i])
            dfs(i, total + nums[i])
            # skip
            cur.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res
