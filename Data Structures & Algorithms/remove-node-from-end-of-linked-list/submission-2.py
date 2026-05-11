# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        nodes = []
        if not head.next:
            return None
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        if len(nodes) - n == 0:
            return head.next
        
        nodes[len(nodes)-n-1].next = nodes[len(nodes) - n].next
        return nodes[0]

