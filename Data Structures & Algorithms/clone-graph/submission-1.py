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
        hashMap = {}
        def dfs(node):
            if not node or node in hashMap:
                return
            cpy = Node(node.val)
            hashMap[node] = cpy
            for n in node.neighbors:
                dfs(n)
        dfs(node)
        for cur in hashMap:
            cpy = hashMap[cur]
            for n in cur.neighbors:
                n_cpy = hashMap[n]
                cpy.neighbors.append(n_cpy)
        return hashMap[node]
            