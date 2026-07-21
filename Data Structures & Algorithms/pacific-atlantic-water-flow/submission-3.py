class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac, atl = set(), set()

        def dfs(row, col, visited, prev):
            if((row, col) in visited or row < 0 or col < 0 or row >= ROWS or col >= COLS):
                return 

            if heights[row][col] >= prev:
                visited.add((row,col))
                dfs(row+1, col, visited, heights[row][col])
                dfs(row-1, col, visited, heights[row][col])
                dfs(row, col+1, visited, heights[row][col])
                dfs(row, col-1, visited, heights[row][col])

        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS - 1, atl, -1)
        
        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS - 1, c, atl, -1)
        
        # both = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r,c) in pac and (r,c) in atl:
        #             both.append([r,c])
        bothSet = pac.intersection(atl)
        both = []
        for entry in bothSet:
            r = entry[0]
            c = entry[1]
            both.append([r,c])
        return both



