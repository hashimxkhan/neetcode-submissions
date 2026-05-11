# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = set()
        res = []

        def dfs(root, level):
            nonlocal res
            nonlocal levels
            if not root:
                return
            
            if level not in levels:
                res.append(root.val)
                levels.add(level)
            dfs(root.right, level+1)
            dfs(root.left, level+1)
        
        dfs(root, 0)
        return res
        