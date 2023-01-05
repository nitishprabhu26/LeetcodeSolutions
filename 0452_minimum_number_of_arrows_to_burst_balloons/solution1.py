# Approach 1: Greedy
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/ (followed this)
# (use picture in example to understand)


from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # sort by x_end
        points.sort(key = lambda x : x[1])
        
        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if x_start > first_end:
                arrows += 1
                first_end = x_end
        
        return arrows


# OR
# https://youtu.be/hND9YHeZJLA

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x : x[1])
        
        count = 0
        ending = float('-inf')
        for balloon in points:
            if balloon[0] > ending:
                count += 1
                ending = balloon[1]
        
        return count


points = [[10,16],[2,8],[1,6],[7,12]]
obj = Solution()
print(obj.findMinArrowShots(points))


# Complexity Analysis:
# Time complexity : O(N.logN) because of sorting of input data.
# Space complexity : O(N) or O(logN)
# The space complexity of the sorting algorithm depends on the implementation of each program language.
# For instance, the list.sort() function in Python is implemented with the Timsort algorithm whose space 
# complexity is O(N). In Java, the Arrays.sort() is implemented as a variant of quicksort algorithm whose 
# space complexity is O(logN).