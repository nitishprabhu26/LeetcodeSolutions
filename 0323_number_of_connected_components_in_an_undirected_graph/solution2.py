# Approach 1: BFS, similar to DFS

from collections import deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
                           
        components = 0
        visited = [False] * n
        
        # creating adjacency list, lists the neighbors of any given node
        # Create an adjacency list such that adj[v] contains all the adjacent vertices of vertex v.
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            
        # Iterate over each vertex in edges, and if the vertex is not already in visited, add it to queue. 
        # Add every vertex visited during the BFS to visited.
        for i in range(n):
            if not visited[i]:
                components += 1
                
                queue = deque([i])
                while queue:
                    index = queue.pop()
                    visited[index] = True
                    for adj in adjList[index]:
                        if not visited[adj]:
                            queue.appendleft(adj)
                
        return components


n = 5
edges = [[0,1],[1,2],[3,4]]
obj = Solution()
print(obj.countComponents(n, edges))

