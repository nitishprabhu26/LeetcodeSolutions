# Approach 2: Using Stack(stack will be in monotonic decreasing order)
# https://www.youtube.com/watch?v=cTBiBSnjO3c
#  A monotonic stack is simply a stack where the elements are always in sorted order.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # pair: [temp,index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                answer[stackInd] = (i-stackInd)
            stack.append([t, i])
        return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
obj = Solution()
print(obj.dailyTemperatures(temperatures))

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         n = len(temperatures)
#         answer = [0] * n
#         stack = []
        
#         for curr_day, curr_temp in enumerate(temperatures):
#             # Pop until the current day's temperature is not
#             # warmer than the temperature at the top of the stack
#             while stack and temperatures[stack[-1]] < curr_temp:
#                 prev_day = stack.pop()
#                 answer[prev_day] = curr_day - prev_day
#             stack.append(curr_day)
        
#         return answer

# Complexity analysis:

# Time complexity : O(n).
# At first glance, it may look like the time complexity of this algorithm should be O(N^2), because there is a nested while loop inside 
# the for loop. However, each element can only be added to the stack once, which means the stack is limited to N pops. Every iteration 
# of the while loop uses 1 pop, which means the while loop will not iterate more than N times in total, across all iterations of the 
# for loop.
# An easier way to think about this is that in the worst case, every element will be pushed and popped once. This gives a time 
# complexity of O(N)O(2⋅N)=O(N).

# Space complexity : O(n).
# If the input was non-increasing, then no element would ever be popped from the stack, and the stack would grow to a size of N elements 
# at the end.
# Note: answer does not count towards the space complexity because space used for the output format does not count.