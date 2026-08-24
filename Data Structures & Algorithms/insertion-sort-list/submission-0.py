# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = ListNode(head.val)
        curr = head.next
        while curr:
            cur = ListNode(curr.val)
            val = curr.val
            new = dummy.next
            prev = dummy
            while new:
                if val >= new.val:
                    if not new.next:
                        new.next = cur
                        cur.next = None
                        break
                    prev = new
                    new = new.next
                else:
                    cur.next = new
                    prev.next = cur
                    break
            curr = curr.next
        return dummy.next

