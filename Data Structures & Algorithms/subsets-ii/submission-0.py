class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        my_set = set()
        def dfs(i):
            if i == len(nums):
                t = tuple(sorted(cur))
                if t not in my_set:
                    res.append(cur.copy())
                    my_set.add(t)
                return
            # decision: choose nums[i]
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return res
