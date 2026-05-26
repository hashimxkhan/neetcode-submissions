# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        q = []
        q.append(root)
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
                if i == 0:
                    ret.append(cur.val)
        return ret

