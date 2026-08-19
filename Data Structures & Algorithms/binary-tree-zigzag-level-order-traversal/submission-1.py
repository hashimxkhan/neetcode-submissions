# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        ret = []
        lev = 0
        if not root:
            return []
        while q:
            new = []
            for _ in range(len(q)):
                cur = q.popleft()
                new.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if lev % 2 == 1:
                new.reverse()
            ret.append(new)
            lev+=1
        return ret