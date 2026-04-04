class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, i_val in enumerate(nums):
            for j, j_val in enumerate(nums):
                if i != j and (i_val + j_val) == target:
                    result.append(i)
                    result.append(j)
                    return result
                    