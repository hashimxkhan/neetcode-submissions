# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        cur = head
        while cur:
            cur = cur.next
            length+=1
        
        cur = head
        k = length // 2
        if length % 2 == 1:
            k = (length // 2) + 1
        i = 1
        while i < k:
            i+=1
            cur = cur.next
        
        return cur

        
