class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i):
            if i >= len(nums) or i < 0:
                return 0
            elif(i in memo):
                return memo[i]
            else:
                memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
                return memo[i]

        maximum = -1
        for i in range(len(nums)):
            curr = dfs(i)
            maximum = max(curr, maximum)
        return maximum
            

