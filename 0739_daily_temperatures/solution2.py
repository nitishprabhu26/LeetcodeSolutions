# Approach 2: Using Stack(stack will be in monotonic decreasing order)
# https://www.youtube.com/watch?v=cTBiBSnjO3c

class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
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


# Complexity analysis:

# Time complexity : O(n).
# Space complexity : O(n).
