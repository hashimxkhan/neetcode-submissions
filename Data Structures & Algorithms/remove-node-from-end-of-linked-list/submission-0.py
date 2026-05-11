# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length+=1
        count = 0
        cur = head
        # case if it is head
        if length - count == n:
            return head.next
        while cur.next:
            if length - count - 1 == n:
                cur.next = cur.next.next
                return head
            cur = cur.next
            count+=1
            

        
        