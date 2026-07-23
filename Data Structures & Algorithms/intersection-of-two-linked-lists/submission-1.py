# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur = headA
        a = []
        b = []
        while cur:
            a.append(cur)
            cur = cur.next
        cur = headB
        while cur:
            b.append(cur)
            cur = cur.next

        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    return a[i]