class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = {}
        def bfs(i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]) and grid[i][j] == '1': 
                    if (i,j) not in visited:
                        nonlocal count
                        visited[(i,j)] = True
                        count += 1
                    visitNeighbors(i,j-1)
                    visitNeighbors(i,j+1)
                    visitNeighbors(i-1,j)
                    visitNeighbors(i+1,j)

        def visitNeighbors(i,j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]) and grid[i][j] == '1' and (i,j) not in visited:
                visited[(i,j)] = True
                bfs(i,j)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                bfs(i, j)
        
        print(visited)
        return count
        

        