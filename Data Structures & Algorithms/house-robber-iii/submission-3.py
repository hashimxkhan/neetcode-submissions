# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        cache = {}
        def dfs(node, taken):
            if not node:
                return 0
            if (node,taken) in cache:
                return cache[(node,taken)]
            if taken:
                cache[(node,taken)] = dfs(node.left, False) + dfs(node.right, False)
            else:
                cache[(node,taken)] = max(dfs(node.left, False) + dfs(node.right, False), node.val + dfs(node.left, True) + dfs(node.right, True))
            return cache[(node,taken)]
        return dfs(root, False)
