# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        i = len(nodes) - n 
        if i == 0:
            return head.next
        prev = nodes[i-1]
        prev.next = nodes[i].next
        return head

