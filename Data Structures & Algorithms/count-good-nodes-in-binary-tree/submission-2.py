# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs returns the number of good nodes in the tree
        def dfs(root, maxi):
            if not root:
                return 0
            
            if root.val >= maxi:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, maxi) + dfs(root.right, maxi)
        
        return dfs(root, float('-inf'))

            

            

