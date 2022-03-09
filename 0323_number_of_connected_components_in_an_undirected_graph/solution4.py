# Approach :Union Find
# Neetcode : https://youtu.be/8f1XPm4WOUc


from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # initially each node is going to be its parent
        par = [i for i in (range(n))]
        # initially all nodes will have rank 1
        rank = [1] * n
        
        # to find the parent of that vertex, and return root parent
        def find(n1):
            res = n1
            # stop looping when node itself is its own parent. i.e we found root parent
            while res != par[res]:
                # go up the chain
                # make parent its grandparent
                par[res] = par[par[res]]
                # update current pointer to its parent
                res = par[res]
            return res
        
        
        def union(n1, n2):
            # find root parents of both nodes
            p1 = find(n1)
            p2 = find(n2)
            
            # if both have same root parents, no union performed here
            if p1 == p2:
                return 0
            
            # successful union performed case
            if rank[p2] > rank[p1]:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            else:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            return 1
                    
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
                
        return res


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