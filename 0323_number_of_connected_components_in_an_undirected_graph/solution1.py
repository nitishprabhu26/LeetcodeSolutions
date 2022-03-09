# Approach 1: Depth-First Search (DFS)
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/solution/ (video)

# In an undirected graph, a connected component is a subgraph in which each pair of vertices is connected via a 
# path. So essentially, all vertices in a connected component are reachable from one another.

# If we run DFS, starting from a particular vertex, it will continue to visit the vertices depth-wise until there 
# are no more adjacent vertices left to visit. Thus, it will visit all of the vertices within the connected 
# component that contains the starting vertex. Each time we finish exploring a connected component, we can find 
# another vertex that has not been visited yet, and start a new DFS from there. The number of times we start a new 
# DFS will be the number of connected components.

# Algorithm
# - Create an adjacency list such that adj[v] contains all the adjacent vertices of vertex v.
# - Initialize a hashmap or array, visited, to track the visited vertices.
# - Define a counter variable and initialize it to zero.
# - Iterate over each vertex in edges, and if the vertex is not already in visited, start a DFS from it. Add 
#   every vertex visited during the DFS to visited.
# - Every time a new DFS starts, increment the counter variable by one.
# - At the end, the counter variable will contain the number of connected components in the undirected graph.


from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            for adj in adjList[node]:
                if not visited[adj]:
                    visited[adj] = True
                    dfs(adj)
                    
        components = 0
        visited = [False] * n
        
        # creating adjacency list, lists the neighbors of any given node
        # Create an adjacency list such that adj[v] contains all the adjacent vertices of vertex v.
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            
        # Iterate over each vertex in edges, and if the vertex is not already in visited, start a DFS from it. 
        # Add every vertex visited during the DFS to visited.
        for i in range(n):
            if not visited[i]:
                components += 1
                visited[i] = True
                dfs(i)
                
        return components


n = 5
edges = [[0,1],[1,2],[3,4]]
obj = Solution()
print(obj.countComponents(n, edges))


# Complexity Analysis:
# Here E = Number of edges, V = Number of vertices.
# Time Complexity: O(E + V).
# Building the adjacency list will take O(E) operations, as we iterate over the list of edges once, and insert 
# each edge into two lists.
# Initializing visited array will take O(V).
# During the DFS traversal, each vertex will only be visited once. This is because we mark each vertex as visited 
# as soon as we see it, and then we only visit vertices that are not marked as visited. In addition, when we 
# iterate over the edge list of each vertex, we look at each edge once. This has a total cost of O(E+V).
# Space Complexity : O(E + V).
# Building the adjacency list will take O(E) space. To keep track of visited vertices, an array of size O(V) is 
# required. Also, the run-time stack for DFS will use O(V) space.