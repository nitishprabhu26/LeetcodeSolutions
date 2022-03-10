# Approach: Neetcode
# https://youtu.be/A8NUOmlwOlM


from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # if the intervals are overlapping, then updat ethe new interval by merging
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res
        

intervals = [[1,3],[6,9]]
newInterval = [2,5]
obj = Solution()
print(obj.insert(intervals, newInterval))


# Complexity Analysis:

# Time complexity : O(N) since it's one pass along the input array.
# Space complexity : O(N) to keep the output.