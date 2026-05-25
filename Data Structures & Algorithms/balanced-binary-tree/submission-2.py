# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.flag = True

        def balanced(node):
            if not node:
                return 0
            
            leftHeight = balanced(node.left)
            rightHeight = balanced(node.right)

            if abs(leftHeight - rightHeight) > 1:
                self.flag = False
            
            return 1 + max(leftHeight, rightHeight)
        
        balanced(root)
        return self.flag