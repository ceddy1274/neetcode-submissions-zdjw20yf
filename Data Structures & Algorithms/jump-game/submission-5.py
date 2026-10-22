class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currIndex = 0
        memo = {}
        def jumpCheck(currIndex):
            if currIndex in memo:
                return memo[currIndex]
            if(currIndex >= (len(nums) - 1)):
                memo[currIndex] = True
                return True
            jumpSpots = nums[currIndex]
            if jumpSpots == 0:
                memo[currIndex] = False
                return False
            
            for i in range(1, jumpSpots+1):
                if(jumpCheck(currIndex + i)):
                    memo[currIndex] = True
                    return True
            memo[currIndex] = False
            return False
        return jumpCheck(currIndex)