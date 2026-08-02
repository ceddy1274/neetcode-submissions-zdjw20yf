# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        count = 0
        slow = head
        fast = head.next

        odd = False
        while(fast and fast.next):
            count += 1
            slow = slow.next
            fast = fast.next.next
            if not fast:
                odd = True
        
        if odd:
            return slow
        return slow.next