# using sort method and lambda function

class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        points.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
        return points[:k]

# points = [[1, 3], [-2, 2]]
# k = 1


points = [[3, 3], [5, -1], [-2, 4]]
k = 2

obj = Solution()
print(obj.kClosest(points, k))

# Time complexity: O(NlogN)