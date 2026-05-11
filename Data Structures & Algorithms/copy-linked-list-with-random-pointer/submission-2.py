"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldcpy = {}
        oldcpy[None] = None
        cur = head
        while cur: # make copu of eachnode and map
            copy = Node(cur.val)
            oldcpy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldcpy[cur]
            copy.next = oldcpy[cur.next]
            copy.random = oldcpy[cur.random]
            cur = cur.next
        return oldcpy[head]