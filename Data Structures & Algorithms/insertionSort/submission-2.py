
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import copy
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        
            
        states = []
        states.append(copy.deepcopy(pairs))
        if len(pairs) <= 1:
            return states
        for i in range(1, len(pairs)):
            curr = pairs[i]
            prev = i - 1
            while prev >= 0 and curr.key < pairs[prev].key:
                pairs[prev+1] = pairs[prev]
                prev -= 1
            pairs[prev+1] = curr
            states.append(copy.deepcopy(pairs))
        
        return states