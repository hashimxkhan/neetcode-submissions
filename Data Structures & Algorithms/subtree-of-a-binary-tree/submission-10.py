# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right):
                return True

            return False
        
        def check(root, subRoot):
            if not root:
                return False

            return dfs(root, subRoot) or check(root.left, subRoot) or check(root.right, subRoot)
        
        return check(root, subRoot)



