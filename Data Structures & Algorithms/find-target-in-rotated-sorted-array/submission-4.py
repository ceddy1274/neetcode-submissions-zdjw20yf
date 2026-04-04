class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if(nums[0] == target):
                return 0
            else:
                return -1
        elif len(nums) == 2:
            if(nums[0] == target):
                return 0
            elif(nums[1] == target):
                return 1
            else:
                return 0
        while(l < r):
            m = l + (r-l) // 2
            if(m == l or m == r):
                return -1
            elif(nums[m] == target):
                return m
            elif(nums[r] == target):
                return r
            elif(nums[l] == target):
                return l
            elif (nums[r] < target):
                r = m
            elif (nums[l] > target):
                l = m + 1
            else:
                return -1



