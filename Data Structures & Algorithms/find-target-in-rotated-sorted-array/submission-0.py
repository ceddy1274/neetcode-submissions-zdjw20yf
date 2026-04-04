class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l < r):
            m = l + (r-l) // 2
            print(l, m, r)
            if(nums[m] == target):
                return m
            elif (nums[r] < target):
                r = m
            elif (nums[l] > target):
                l = m + 1
            else:
                return -1



