# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        first = ""
        while cur:
            first+= str(cur.val)
            cur = cur.next
        
        cur = l2
        second = ""
        while cur:
            second+= str(cur.val)
            cur = cur.next
        
        ans = int(first) + int(second)
        ans = str(ans)

        l3 = ListNode()
        cur = l3
        i = 0
        while i < len(ans) - 1:
            cur.val = ans[i]
            cur.next = ListNode()
            cur = cur.next
            i+=1
        cur.val = ans[i]
        return l3
