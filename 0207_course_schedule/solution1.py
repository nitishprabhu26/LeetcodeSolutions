# Neetcode
# https://youtu.be/EgI5nU9etnU

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # match each course to prereq list
        preMap = { i:[] for i in range(numCourses) }
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
            
        # visitSet = stores all courses along the curr DFS
        visitSet = set()
        
        def dfs(crs):
            # visiting a course twice - loop detected
            if crs in visitSet:
                return False
            # if a course has no prereqs, then it can be completed
            if preMap[crs] == []:
                return True
            
            
            visitSet.add(crs)
            # run dfs for each of its prereqs
            for pre in preMap[crs]:
                # return False immediately if any one of the course cant be completed
                if not dfs(pre): return False
            
            # else it can be a course that can be taken
            # So, remove from visit set; set the premap list to empty for that course since we know that it can be completed
            # and then return True
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        # call dfs for every single course in numCourses
        # looping reason - what if graph is not fully connected
        # eg:
        #     1 -> 2
        #     3 -> 4
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            
numCourses = 2 
prerequisites = [[1,0]]

# numCourses = 2
# prerequisites = [[1,0],[0,1]]

obj = Solution()
print(obj.canFinish(numCourses, prerequisites))


# Complexity analysis:
# Time complexity : O(n+p). 
# i.e. O( ∣E∣ + ∣V∣ ) where |V| is the number of courses, and |E| is the number of dependencies.
# n - no of nodes, p - no of prereqs.
# Space complexity : O(p). p - no of prereqs.