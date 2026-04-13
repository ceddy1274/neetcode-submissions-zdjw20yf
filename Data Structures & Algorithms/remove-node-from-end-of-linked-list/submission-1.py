# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while(curr):
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Reverse
        head = self.reverse(head)

        #Remove
        if(n == 1):
            headNext = head.next
            head.next = None
            head = headNext
        currTraverseNode = head
        for i in range(n-1):
            prevTraverseNode = currTraverseNode
            currTraverseNode = currTraverseNode.next
        if(n > 1):
            prevTraverseNode.next = currTraverseNode.next

        #Reverse
        head = self.reverse(head)
        return head