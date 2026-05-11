class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        my_set = set()
        def dfs(i, cur):
            if i == len(candidates):
                total = 0
                for num in cur:
                    total+= num
                if total == target:
                    t = tuple(sorted(cur.copy()))
                    if t not in my_set:
                        res.append(cur.copy())
                    my_set.add(t)
                return
            # choose i
            cur.append(candidates[i])
            dfs(i+1, cur)
            # not choose
            cur.pop()
            dfs(i+1, cur)
        dfs(0, [])
        return res
        