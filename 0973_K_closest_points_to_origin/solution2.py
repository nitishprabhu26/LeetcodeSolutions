# Using heapq
# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
# https://leetcode.com/problems/k-closest-points-to-origin/solutions/348171/Python3-sort-O(NlogN)-minimum-heap-O(NlogN)-and-maximum-heap-O(NlogK)/


import heapq
from typing import List

# Using heapq and nsmallest function
class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        return heapq.nsmallest(k, points, key = lambda x: (x[0] * x[0] + x[1] * x[1]))

# OR

# Using heappush and heappop
# Time Complexity: O(N.logN)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for point in points:
            heapq.heappush(distance, (point[0]**2 + point[1]**2, point))
        K_points = []
        for i in range(k):
            K_points.append(heapq.heappop(distance)[1])
        return K_points

# OR
# The problem is we still sorted all the element, the time complexity is O(NlogN) .Still we only need the 
# top k smallest element. We don't need to take of other elements' order. So if we keep a size of k's heap, 
# use the heap[0] element as threshhold, interate through the array, only those meet the requirment element get 
# into the heap.
# Time compiexity: O(N.logK)
# Since python3 doesn't have a build-in maximum heap, so we use the minimum heap to achieve maximum heap's 
# property. Here, we keep a heap with size of K. So we can improve the time complexity to O(N.logK).
# heapq is a binary heap, with O(log n) push and O(log n) pop. n is the size of the minimum heap. 
# In this case, n = K.
# So the time complexity is N.log(K)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for p in points:
            if len(distance) <= k - 1:
                heapq.heappush(distance, ( -p[0]**2-p[1]**2, p))
            else:
                if - p[0]**2 - p[1]**2 > distance[0][0]:
                    heapq.heappop(distance)
                    heapq.heappush(distance,( -p[0]**2-p[1]**2, p))
        res = []
        for i in range (k):
            res.append(heapq.heappop(distance)[1])
        return res


# points = [[1, 3], [-2, 2]]
# k = 1
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
obj = Solution()
print(obj.kClosest(points, k))


# Complexity Analysis:
# Time Complexity: O(N.logN), intuitively use minimum Heap:
# make a maximum-heap to store distance, (point's distance to original, point)
# each time call heapq.heappop (distance), it will pop the smallest item in the heap. So heappop K times will 
# be the result.
# Space Complexity: O(N).