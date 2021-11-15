from typing import List

# Approach 1: Brute force - Time limit exceeded for large input
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         n = len(temperatures)
#         answer = [0] * n
#         for i in range(0, n):
#             for j in range(i+1, n):
#                 if temperatures[i] < temperatures[j]:
#                     answer[i] = j-i
#                     break
#         return answer

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        for today in range(n):
            for futureDay in range(today+1, n):
                if temperatures[futureDay] > temperatures[today]:
                    output[today] = futureDay - today
                    break
        return output


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
obj = Solution()
print(obj.dailyTemperatures(temperatures))

# Complexity analysis:

# Time complexity : O(n^2). For every temperature value, look throgh the etire rest of the array on the right.
# Space complexity : O(n).
