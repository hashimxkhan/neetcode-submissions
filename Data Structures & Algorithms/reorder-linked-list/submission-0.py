# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list2 = slow.next
        prev = slow.next = None # sever them both
        cur = list2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        list2 = prev
        list1 = head
        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2





        