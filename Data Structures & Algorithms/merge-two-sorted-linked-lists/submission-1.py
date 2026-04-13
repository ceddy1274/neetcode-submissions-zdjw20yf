# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currList1 = list1
        currList2 = list2
        if(currList1 == None):
            return list2
        if(currList2 == None):
            return list1
        if(currList2.val <= currList1.val):
            list3 = ListNode(currList2.val)
            currList2 = currList2.next
            if(currList2 == None):
                list3.next = currList1
                return list3
        elif(currList1.val < currList2.val):
            list3 = ListNode(currList1.val)
            currList1 = currList1.next
            if(currList1 == None):
                list3.next = currList2
                return list3
        head = list3
        while(currList1 != None or currList2 != None):
            if(currList2.val <= currList1.val):
                list3.next = currList2
                list3 = list3.next
                currList2 = currList2.next
                if(currList2 == None):
                    list3.next = currList1
                    return head
            elif(currList1.val < currList2.val):
                list3.next = currList1
                list3 = list3.next
                currList1 = currList1.next
                if(currList1 == None):
                    list3.next = currList2
                    return head
