class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      lengthNums = len(nums)
      numsSet = set()
      if lengthNums < 2:
        return False
      for i in range(lengthNums):
        curr = nums[i] 
        numsSet.add(curr)
      return (len(numsSet) != lengthNums)