# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        i = 0
        j = len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            nodes[j].next = nodes[i+1]
            i+=1
            j-=1
        nodes[i].next = None
        