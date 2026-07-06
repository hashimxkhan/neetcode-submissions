# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        length = 1
        while cur and cur.next:
            cur = cur.next
            length+=1
        if length <= 1:
            return head
        
        if k >= length:
            k = k % length
        if k == 0:
            return head

        cur.next = head
        i = 1
        cur = head
        while i < length - k:
            cur = cur.next
            i+=1
        nxt = cur.next
        cur.next = None
        return nxt
