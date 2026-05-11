# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            if leftMax < 0:
                leftMax = 0
            if rightMax < 0:
                rightMax = 0
            cur = node.val + leftMax + rightMax
            if cur > maxSum:
                maxSum = cur
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return maxSum
            