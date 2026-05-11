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
        
        nodeIndex = len(nodes) - n
        if nodeIndex == 0:
            return head.next
        
        nodes[nodeIndex-1].next = nodes[nodeIndex].next
        return head

