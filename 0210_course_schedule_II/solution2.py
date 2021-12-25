# Neetcode similar to old code(course schedule 1) (FASTER THAN SOLUTION 1)
# https://youtu.be/Akt3glAwyfY

# crs in output - O(n),
# so we use visit (set()) so lookup comes down to O(1) (FASTER THAN SOLUTION 1)
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # match each course to prereq list - adjacency list
        preMap = { c:[] for c in range(numCourses) }
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # print(preMap)
            
        # a course has 3 possible states
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle

        # visitSet = stores all courses along the curr DFS
        visit, cycle = set(), set()
        # stores output path
        output = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            
            # run dfs for each of its prereqs
            for pre in preMap[crs]:
                # return False immediately if any one of the course cant be completed
                if not dfs(pre): return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            
            return True
        
        # call dfs for every single course in numCourses
        # looping reason - what if graph is not fully connected
        # eg:
        #     1 -> 2
        #     3 -> 4
        for crs in range(numCourses):
            if not dfs(crs): return []
        return output
            
numCourses = 2 
prerequisites = [[1,0]]

# numCourses = 2
# prerequisites = [[1,0],[0,1]]

obj = Solution()
print(obj.findOrder(numCourses, prerequisites))


# Complexity analysis:
# Time complexity : O(n+p). 
# i.e. O( ∣E∣ + ∣V∣ ) where |V| is the number of courses, and |E| is the number of dependencies.
# n - no of nodes, p - no of prereqs.
# Space complexity : O(p). p - no of prereqs.