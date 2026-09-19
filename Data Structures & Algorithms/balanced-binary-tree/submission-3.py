# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True
        def height(node):
            if not node:
                return 0
            
            left = 1 + height(node.left)
            right = 1 + height(node.right)
            if abs(left - right) > 1:
                print(left)
                print(right)
                self.balanced = False
            return max(left, right)
        
        height(root)
        return self.balanced
