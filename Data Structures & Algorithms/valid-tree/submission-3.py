class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        adjList = {i:[] for i in range(n)}

        for edge in edges:
            i = edge[0]
            j = edge[1]
            adjList[i].append(j)
            adjList[j].append(i)
        
        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False

            visited.add(curr)
            for neighbor in adjList[curr]:
                if neighbor == prev:
                    continue
                elif not dfs(neighbor, curr):
                    return False
            return True
        
        return (dfs(0, -1) and len(visited) == n)