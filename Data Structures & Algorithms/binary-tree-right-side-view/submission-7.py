# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = set()
        ret = []
        def dfs(node, level):
            if not node:
                return
            
            if level not in levels:
                ret.append(node.val)
                levels.add(level)
            dfs(node.right, level+1)
            dfs(node.left, level+1)

        dfs(root, 0)
        return ret