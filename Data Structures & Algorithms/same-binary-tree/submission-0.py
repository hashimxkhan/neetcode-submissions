# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qQ = deque()
        pQ = deque()
        qQ.append(q)
        pQ.append(p)
        while pQ and qQ:
            pRoot = pQ.popleft()
            qRoot = qQ.popleft()
            if qRoot is None and pRoot is None:
                continue
            if pRoot is None or qRoot is None or pRoot.val != qRoot.val:
                return False
            pQ.append(pRoot.left)
            pQ.append(pRoot.right)
            qQ.append(qRoot.left)
            qQ.append(qRoot.right)
        if pQ or qQ:
            return False
        return True


