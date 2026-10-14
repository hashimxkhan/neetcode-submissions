# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n) memory
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        
        if n == len(arr):
            return head.next
        
        arr[len(arr) - n - 1].next = arr[len(arr) - n].next
        return head
        

        
        