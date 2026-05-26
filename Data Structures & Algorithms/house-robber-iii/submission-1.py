# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def dfs(node, take):

            if not node:
                return 0
            if (node,take) in cache:
                return cache[(node,take)]
            
            if take:
                cache[(node,take)] = node.val + dfs(node.right, False) + dfs(node.left, False)
            else:
                cache[(node, take)] = max(dfs(node.left, True), dfs(node.left, False)) + max(dfs(node.right, False), dfs(node.right, True))
            return cache[(node,take)]

        return max(dfs(root, True), dfs(root, False))