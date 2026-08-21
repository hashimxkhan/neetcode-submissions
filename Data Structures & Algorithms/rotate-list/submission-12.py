# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        arr = []
        if not head:
            return None
        if k == 0:
            return head
        while cur:
            arr.append(cur)
            cur = cur.next
        if len(arr) == k:
            return head
        
        if k > len(arr):
            k = k % len(arr)
        if len(arr) == 1:
            return head
        print(len(arr) - k - 1)
        arr[len(arr) - k - 1].next = None
        arr[len(arr)-1].next = arr[0]
        return arr[len(arr)- k]
        

