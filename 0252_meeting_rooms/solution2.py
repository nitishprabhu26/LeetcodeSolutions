# Approach 2: Sorting
# The idea here is to sort the meetings by starting time. Then, go through the meetings one by one and make 
# sure that each meeting ends before the next one starts.
# or 
# Neetcode
# https://youtu.be/PaJxqZVPhbg

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        # intervals.sort(key= lambda i: i[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


intervals = [[0, 30], [5, 10], [15, 20]]
obj = Solution()
print(obj.canAttendMeetings(intervals))

# Complexity Analysis

# Time complexity : O(nlogn). The time complexity is dominated by sorting. Once the array has been sorted, 
# only O(n) time is taken to go through the array and determine if there is any overlap.
# Space complexity : O(1). Since no additional space is allocated.
