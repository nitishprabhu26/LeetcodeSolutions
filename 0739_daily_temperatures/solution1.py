# Approach 1: Brute force - Time limit exceeded for large input
class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        n = len(temperatures)
        answer = [0] * n
        for i in range(0, n):
            for j in range(i+1, n):
                if temperatures[i] < temperatures[j]:
                    answer[i] = j-i
                    break
        return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
obj = Solution()
print(obj.dailyTemperatures(temperatures))


# Complexity analysis:

# Time complexity : O(n^2). For every temperature value, look throgh the etire rest of the array on the right.
# Space complexity : O(n).
