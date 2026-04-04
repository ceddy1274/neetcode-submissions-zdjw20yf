class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         unique = {}
         for i in range(len(nums)):
            curr = nums[i]
            try:
                unique[curr] += 1
            except:
                unique[curr] = 1
         sortedUnique = sorted(unique.items(), key=lambda item: item[1], reverse=True)
         res = []
         for i in range(k):
            res.append(sortedUnique[i][0])
         return res