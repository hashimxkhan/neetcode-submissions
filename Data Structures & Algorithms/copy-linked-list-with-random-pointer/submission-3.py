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
        cpymap = {}
        cpymap[None] = None
        cur = head
        while cur:
            cpy = Node(cur.val)
            cpymap[cur] = cpy
            cur = cur.next

        for key in cpymap:
            if key:
                cpymap[key].next = cpymap[key.next]
                cpymap[key].random = cpymap[key.random]
        
        return cpymap[head]