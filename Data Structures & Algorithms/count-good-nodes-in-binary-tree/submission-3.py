# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, maxi):
            if not node:
                return 0
            if node.val >= maxi:
                self.res+=1
                maxi = node.val
            dfs(node.left, maxi)
            dfs(node.right, maxi)
        
        dfs(root, float('-inf'))
        return self.res