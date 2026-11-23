# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() 
        s,f = head,head
        while s and f: 
            if f.next != None:
                fnext = f.next
            elif f.next == None:
                return False
            if s.next == fnext.next:
                return True
            else:
                seen.add(s)
                seen.add(f)
            s = s.next
            f = fnext.next
        return False