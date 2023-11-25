# Neetcode: Using minheap
# https://youtu.be/rI2EBUEMfTk?si=YNmNggCXKzMSsioT


import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])

        # O(N) time
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res


# points = [[1, 3], [-2, 2]]
# k = 1
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
obj = Solution()
print(obj.kClosest(points, k))


# Complexity Analysis:
# Time Complexity: O(N + K.logN), where N is the length of points.
# Space Complexity: O(N).