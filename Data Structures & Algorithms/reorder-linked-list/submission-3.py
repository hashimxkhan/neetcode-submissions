# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        
        n = len(arr)
        for i in range((n//2)):
            arr[i].next = arr[n-i-1]
            arr[n-i-1].next = arr[i+1]
        arr[n//2].next = None