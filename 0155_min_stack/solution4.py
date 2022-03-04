# Approach : Neetcode
# https://youtu.be/qkLl7nAwDPo


from typing import List

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(7)
obj.push(14)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.stack)
print(obj.pop())
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
print(obj.stack)


# Complexity Analysis:
# Time Complexity : O(1) for all operations. Same as Approach 1.
# Space Complexity : O(n). Same as Approach 1.