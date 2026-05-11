class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            # base case
            if i == len(nums):
                res.append(cur.copy()) # no pruning as we want all subsets
                return
            # decision
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
            dfs(i+1, cur)
        dfs(0, [])
        return res
            

        