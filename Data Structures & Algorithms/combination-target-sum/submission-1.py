class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        def backtrack(i):
            if i >= len(nums) or sum(combo) >= target:
                if sum(combo) == target:
                    res.append(combo[::])
                return
            combo.append(nums[i])
            if sum(combo) <= target:
                backtrack(i)
            else:
                backtrack(i+1)
            combo.pop()
            backtrack(i+1)
        backtrack(0)
        return res