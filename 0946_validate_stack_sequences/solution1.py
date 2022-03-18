# Approach 1: Greedy

# Algorithm:
# - For each value, push it to the stack.
# - Then, greedily pop values from the stack if they are the next values to pop.
# - At the end, we check if we have popped all the values successfully.


from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            # j < len(popped) is redundant when pushed.length == popped.length is guaranteed.
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
        # check is stack is empty
        # return not stack


pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
obj = Solution()
print(obj.validateStackSequences(pushed, popped))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of pushed and popped.
# Space Complexity: O(N).