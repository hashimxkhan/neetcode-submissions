# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        cur = l1
        while cur:
            num1+=str(cur.val)
            cur = cur.next
        num1 = num1[::-1]
        print(num1)
        cur = l2
        while cur:
            num2+=str(cur.val)
            cur = cur.next
        num2 = num2[::-1]
        total = int(num1) + int(num2)
        total = str(total)
        total = total[::-1]
        list3 = ListNode()
        cur = list3
        for i in range(len(total)-1):
            cur.val = total[i]
            cur.next = ListNode()
            cur = cur.next
        
        cur.val = total[len(total)-1]
        return list3
