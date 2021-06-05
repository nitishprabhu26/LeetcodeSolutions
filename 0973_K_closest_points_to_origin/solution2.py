# Using heapq and nsmallest function
import heapq

class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        return heapq.nsmallest(k, points, key=lambda x: (x[0]*x[0]+x[1]*x[1]))

# points = [[1, 3], [-2, 2]]
# k = 1


points = [[3, 3], [5, -1], [-2, 4]]
k = 2

obj = Solution()
print(obj.kClosest(points, k))
