# Approach 1: Brute Force (TLE in leetcode - 77/78 test cases passed)
# eg:
# 2 meetings: (a,b) & (c,d)
# check a<=c:
#     if b<=c: no overlap
#     if b>c: overlap

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                int1 = intervals[i]
                int2 = intervals[j]
                if (int1[0] <= int2[0] and int1[1] > int2[0]
                        or int2[0] <= int1[0] and int2[1] > int1[0]):
                    return False
        return True


intervals = [[0,30],[5,10],[15,20]]
obj = Solution()
print(obj.canAttendMeetings(intervals))

# Complexity Analysis

# Time complexity: Because we have two check every meeting with every other meeting, the total run time is 
# O(n^2)
# Space complexity: No additional space is used, so the space complexity is O(1).