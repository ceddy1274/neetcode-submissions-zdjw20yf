class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # At each spot calculate if you go down or right
        # If that path eventually leads to the goal add one
        # If it doesn't add none
        memo = {i : -1 for i in range(m * n)}
        
        def findPaths(currMove):
            if(memo[currMove] != -1):
                return memo[currMove]
            if(currMove == ((m*n)-1)):
                return 1
            print(currMove)
            numberOfPaths = 0
            # can we go down
            if((currMove + n) < (m*n)):
                numberOfPaths += findPaths(currMove + n)
            # can we go right
            if(((currMove + 1) % n) != 0):
                numberOfPaths += findPaths(currMove +1)
            memo[currMove] = numberOfPaths
            return numberOfPaths
        
        return findPaths(0)
        