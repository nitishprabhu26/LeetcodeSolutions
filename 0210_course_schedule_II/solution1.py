# Neetcode similar to old code(course schedule 1)
# https://youtu.be/Akt3glAwyfY

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # match each course to prereq list - adjacency list
        preMap = { c:[] for c in range(numCourses) }
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # print(preMap)
            
        # visitSet = stores all courses along the curr DFS
        visitSet = set()
        # stores output path
        output = []
        
        def dfs(crs):
            if crs in visitSet:
                return False
            if crs in output:
                return True
            # optional: saves some iteration and also saves code execution from next line until output.append()
            # ----uncomment----
            # if preMap[crs] == []:
            #     output.append(crs)
            #     return True
            # ----uncomment----

            print(crs)
            visitSet.add(crs)
            
            # run dfs for each of its prereqs
            for pre in preMap[crs]:
                # return False immediately if any one of the course cant be completed
                if not dfs(pre): return False
            
            visitSet.remove(crs)
            output.append(crs)
            # optional: saves code execution until here for some iteration
            # ----uncomment----
            # preMap[crs] = []
            # ----uncomment----
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