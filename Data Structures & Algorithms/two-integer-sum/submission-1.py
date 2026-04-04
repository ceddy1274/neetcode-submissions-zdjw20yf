class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                j = seen[difference]
                return [j, i]
            else:
                seen[num] = i
        return None