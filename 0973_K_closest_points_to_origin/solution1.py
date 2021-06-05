class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        x2, y2 = 0, 0
        result = []
        res = []
        for point in points:
            result.append(
                [pow(point[0] - x2, 2) + pow(point[1] - y2, 2), point])
        result.sort(key=lambda x: x[0])
        for i in result[:k]:
            res.append(i[1])
        return res


# points = [[1, 3], [-2, 2]]
# k = 1

points = [[3, 3], [5, -1], [-2, 4]]
k = 2

obj = Solution()
print(obj.kClosest(points, k))
