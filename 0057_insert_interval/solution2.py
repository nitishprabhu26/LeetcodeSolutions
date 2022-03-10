# Approach: 
# O(nlgn) time, the same as Merge Intervals 
# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        res = []
        for i in sorted(intervals, key=lambda x:x[0]):
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res


intervals = [[1,3],[6,9]]
newInterval = [2,5]
obj = Solution()
print(obj.insert(intervals, newInterval))


# Complexity Analysis:
# Time complexity : O(nlgn). Other than the sort invocation, we do a simple linear scan of the list, so the 
# runtime is dominated by the O(nlogn) complexity of sorting.
# Space complexity : O(logN) or O(N).
# If we can sort intervals in place, we do not need more than constant additional space, although the sorting 
# itself takes O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.