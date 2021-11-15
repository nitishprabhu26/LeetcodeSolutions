# Approach 2: Array, Optimized Space
# Intuition:
# With the monotonic stack, we iterated forward through the array and moved backwards when we found a warmer day. In this approach, 
# we'll do the reverse - iterate backwards through the array, and move forwards to find the number of days until a warmer day.

# https://leetcode.com/problems/daily-temperatures/solution/
# In the first approach, answer exists only to hold the answer. An important thing to notice is that answer carries information that we 
# can use to solve the problem. We can save space and replace the functionality of the stack by using information from answer.


# Algorithm:

# -   Initialize an array answer with the same length as temperatures and all values initially set to 0. Also, initialize an 
#     integer hottest = 0 to track the hottest temperature seen so far.

# -   Iterate backwards through the input. At each index currDay, check if the current day is the hottest one seen so far. If it is, 
#     update hottest and move on. Otherwise, do the following:
#     -     Initialize a variable days = 1 because the next warmer day must be at least one day in the future.
#     -     While temperatures[currDay + days] <= temperatures[currDay]:
#               Add answer[currDay + days] to days. This effectively jumps directly to the next warmer day.
#     -     Set answer[currDay] = days.

# -   Return answer.


from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            # if curr_day is the hottest, then there wont be any other days which will be greater than curr_day temperature
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
obj = Solution()
print(obj.dailyTemperatures(temperatures))


# Complexity Analysis:

# Given N as the length of temperatures,

# Time complexity: O(N)
# Similar to the first approach, the nested while loop makes this algorithm look worse than O(N). However, same as in the first approach, 
# the total number of iterations in the while loop does not exceed N, which gives this algorithm a time complexity of  O(N)O(2⋅N)=O(N).

# Space complexity: O(1).
# As stated above, while answer does use O(N) space, the space used for the output does not count towards the space complexity. Thus, 
# only constant extra space is used.