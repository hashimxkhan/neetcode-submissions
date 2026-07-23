# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        arr1 = []
        arr2 = []
        while cur:
            arr1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            arr2.append(cur.val)
            cur = cur.next
        
        arr1.reverse()
        arr2.reverse()
        s1 = ""
        for a in arr1:
            s1 +=str(a)
        
        s2 = ""
        for a in arr2:
            s2+= str(a)

        s3 = int(s1) + int(s2)
        s3 = str(s3)

        new = ListNode()
        head = new
        for i in range(len(s3)-1, -1, -1):
            new.val = int(s3[i])
            if i == 0:
                break
            new.next = ListNode()
            new = new.next
        
        return head