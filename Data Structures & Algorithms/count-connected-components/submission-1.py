class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = {i:False for i in range(n)}
        adjList = {i:[] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def dfs(num):
            if visited[num]:
                return
            visited[num] = True
            for neighbor in adjList[num]:
                dfs(neighbor)

        connectedComponents = 0
        for num in range(n):
            if not visited[num]:
                dfs(num)
                connectedComponents += 1
        return connectedComponents
        
        