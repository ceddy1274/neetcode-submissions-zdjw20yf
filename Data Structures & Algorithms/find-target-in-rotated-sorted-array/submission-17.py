class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l <= r):
            m = l + (r-l) // 2
            # found target
            if(nums[m] == target):
                return m
            # left half sorted
            if(nums[m] >= nums[l]):
                # binary search left half
                if(target < nums[m] and target >= nums[l]):
                    r = m - 1
                else:
                    l = m + 1
            else:
                # binary search right half
                if(target > nums[m] and target <= nums[r]):
                    l = m + 1
                else:
                    r = m - 1
        return -1

                
        
      


