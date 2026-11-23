# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head,head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        second = s.next
        prev = s.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first,second = head,prev
        while second:
            nxt1,nxt2 = first.next,second.next
            first.next = second
            second.next = nxt1
            first,second = nxt1,nxt2  