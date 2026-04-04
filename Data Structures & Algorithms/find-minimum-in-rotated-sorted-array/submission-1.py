class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = 1

        while(nums[left] < nums[right]):          
            left += 1
            right += 1
            if right >= len(nums):
                return nums[0]
        return nums[right]
