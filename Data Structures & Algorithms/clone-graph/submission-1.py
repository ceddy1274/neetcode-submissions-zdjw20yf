"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        deepCopy = Node(node.val)
        visited[node] = deepCopy

        def dfs(currNode, currDeepNode):
            if not currNode:
                return 
            for curr in currNode.neighbors:
                if curr and curr not in visited:
                    deepCopy = Node(curr.val)
                    visited[curr] = deepCopy
                    currDeepNode.neighbors.append(deepCopy)
                    dfs(curr, deepCopy)
                if curr and curr in visited:
                    deepCopy = visited[curr]
                    if deepCopy not in currDeepNode.neighbors:
                        currDeepNode.neighbors.append(deepCopy)

        dfs(node, deepCopy)
        return deepCopy

        
            