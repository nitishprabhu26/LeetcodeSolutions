# Approach 1: Two Arrays
# https://leetcode.com/problems/find-the-town-judge/solution/

# In graph theory, we say the outdegree of a vertex (person) is the number of directed edges going out of it. For 
# this graph, the outdegree of the vertex represents the number of other people that the person trusts.
# Likewise, we say that the indegree of a vertex (person) is the number of directed edges going into it. So here, 
# it represents the number of people who trust the person.

# We can define the town judge in terms of indegree and outdegree.
# The town judge has an outdegree of 0 and an indegree of N - 1 because they trust nobody, and everybody trusts 
# them (except themselves).
# Therefore, this problem simplifies to calculating the indegree and outdegree for each person and then checking 
# whether or not any of them meet the criteria of the town judge.

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
    
        # people numbered from 1 to N
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
            
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
            
        return -1


n = 3
trust = [[1,3],[2,3]]
obj = Solution()
print(obj.findJudge(n, trust))


# Complexity Analysis:
# Let N be the number of people, and E be the number of edges (trust relationships).

# Time Complexity : O(E).
# We loop over the trust list once. The cost of doing this is O(E).
# We then loop over the people. The cost of doing this is O(N).
# Going by this, it now looks this is one of those many graph problems where the cost is O(max(N,E)) = O(N+E). 
# After all, we don't know whether E or N is the bigger.
# However, we terminate early if E < N - 1. This means that in the best case, the time complexity is O(1). And in 
# the worst case, we know that E ≥ N - 1. Therefore, drop the N, leaving O(E).

# Space Complexity : O(N).
# We allocated 2 arrays; one for the indegrees and the other for the outdegrees. Each was of length N + 1. 
# So O(N).
