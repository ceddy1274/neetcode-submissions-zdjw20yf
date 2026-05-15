class Solution:
    memo = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if n in self.memo.keys():
            return self.memo[n] 
        else:
            minusOne = self.climbStairs(n-1)
            minusTwo = self.climbStairs(n-2)
            self.memo[n] = minusOne + minusTwo
            return (minusOne + minusTwo)