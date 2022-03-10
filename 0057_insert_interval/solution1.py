# Approach 1: Greedy.
# https://leetcode.com/problems/insert-interval/solution/

# Algorithm:
# The straightforward one-pass strategy could be implemented in three steps:
# - Add to the output, all the intervals starting before newInterval.
# - Add to the output, newInterval. Merge it with the last added interval if newInterval starts before the last 
#   added interval ends.
# - Add the next intervals one by one. Merge with the last added interval if the current interval starts before 
#   the last added interval ends.


from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        
        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
            
        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)
            
        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output

        
intervals = [[1,3],[6,9]]
newInterval = [2,5]
obj = Solution()
print(obj.insert(intervals, newInterval))


# Complexity Analysis:

# Time complexity : O(N) since it's one pass along the input array.
# Space complexity : O(N) to keep the output.