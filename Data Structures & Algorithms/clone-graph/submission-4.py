"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # first clone all nodes and map original to clone
        if not node:
            return
        root = node
        visited = {}
        def dfs(node):
            if not node or node in visited:
                return
            cpy = Node(node.val)
            visited[node] = cpy
            for n in node.neighbors:
                dfs(n)
        dfs(node) 
        for node in visited:
            cpy = visited[node]
            for n in node.neighbors:
                cpy.neighbors.append(visited[n])
        return visited[root]