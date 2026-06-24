# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        l = 0
        r = len(arr) - 1
        best = 0
        while l < r:
            best = max(best, arr[l] + arr[r])
            r-=1
            l+=1
        return best