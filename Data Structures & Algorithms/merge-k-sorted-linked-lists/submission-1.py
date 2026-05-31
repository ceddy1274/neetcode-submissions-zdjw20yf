# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        currSmallestValues = []
        # (value, list index)
        for currListIndex, currList in enumerate(lists):
            currSmallestValues.append((currList.val, currListIndex))
            
        heapq.heapify(currSmallestValues)
        sortedListMerge = []
        while currSmallestValues:
            currTuple = heapq.heappop(currSmallestValues)

            currValue = currTuple[0]
            sortedListMerge.append(currValue)

            currList = currTuple[1]
            
            lists[currList] = lists[currList].next
            if lists[currList]:
                newValue = lists[currList].val
                heapq.heappush(currSmallestValues, (newValue, currList))
        mergedKLists = ListNode(0)
        header = mergedKLists
        for i in range(len(sortedListMerge)):
            mergedKLists.val = sortedListMerge[i]
            if i < (len(sortedListMerge)-1):
                mergedKLists.next = ListNode(0)
                mergedKLists = mergedKLists.next
        
        return header