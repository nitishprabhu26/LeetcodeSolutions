# Approach 2: Disjoint Set Union (DSU)
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/solution/ (video)

# Algorithm:
# - Initialize a variable count with the number of vertices in the input.
# - Traverse all of the edges one by one, performing the union-find method combine on each edge. If the endpoints 
#   are already in the same set, then keep traversing. If they are not, then decrement count by 1.
# - After traversing all of the edges, the variable count will contain the number of components in the graph.


from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # to find the parent of that vertex, and return parent
        def find(vertex):
            if vertex == representative[vertex]:
                return vertex
            representative[vertex] = find(representative[vertex])
            return representative[vertex]
            
        def combine(vertex1, vertex2):
            vertex1 = find(vertex1)
            vertex2 = find(vertex2)
            
            if vertex1 == vertex2:
                return 0
            else:
                if size[vertex1] > size[vertex2]:
                    size[vertex1] += size[vertex2]
                    representative[vertex2] = vertex1
                else:
                    size[vertex2] += size[vertex1]
                    representative[vertex1] = vertex2
                return 1
                    
        representative = list(range(n))
        size = [1] * n
        
        components = n
        
        for a, b in edges:
            components -= combine(a, b)
                
        return components


n = 5
edges = [[0,1],[1,2],[3,4]]
obj = Solution()
print(obj.countComponents(n, edges))


# Complexity Analysis:
# Here E = Number of edges, V = Number of vertices.
# Time complexity: O(E⋅α(n)).
# Iterating over every edge requires O(E) operations, and for every operation, we are performing the combine 
# method which is O(α(n)), where α(n) is the inverse Ackermann function.
# Space complexity: O(V).
# Storing the representative/immediate-parent of each vertex takes O(V) space. Furthermore, storing the size of 
# components also takes O(V) space.