# Approach #1: Stack [Accepted]
# OR
# Neetcode: https://youtu.be/Id_tqGdsZQI

# Intuition and Algorithm:
# Let's maintain the value of each valid round on a stack as we process the data. A stack is ideal since we only 
# deal with operations involving the last or second-last valid round.


from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)

        
ops = ["5","-2","4","C","D","9","+","+"]
obj = Solution()
print(obj.calPoints(ops))


# Complexity Analysis:
# Time complexity : O(N), where N is the length of ops. We parse through every element in the given array once, 
# and do O(1) work for each element.
# Space complexity : O(N), the space used to store our stack.
