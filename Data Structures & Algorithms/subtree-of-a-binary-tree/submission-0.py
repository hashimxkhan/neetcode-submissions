# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    from collections import deque
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        return (self.sameTree(root.right, subRoot.right) and self.sameTree(root.left, subRoot.left))
            

