class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        numsList1 = nums[:len(nums)-1]
        numsList2 = nums[1:]
        
        memo1 = {}
        memo2 = {}

        def dfs(i, memo, numsList):
            if i >= len(numsList) or i < 0:
                return 0
            elif i in memo:
                return memo[i]
            else:
                memo[i] = max(numsList[i] + dfs(i+2, memo, numsList), dfs(i+1, memo, numsList))
                return memo[i]
        
        currMax = 0
        for i in range(len(numsList1)):
            currMax = max(dfs(i, memo1, numsList1), currMax)
        for i in range(len(numsList2)):
            currMax = max(dfs(i, memo2, numsList2), currMax)
        return currMax