# Approach 3: Improved Two Stacks

# In the previous approach, we pushed a new number onto the min-tracker Stack if, and only if, it was less than 
# or equal to the current minimum.
# One downside of this solution is that if the same number is pushed repeatedly onto MinStack, and that number 
# also happens to be the current minimum, there'll be a lot of needless repetition on the min-tracker Stack.

# An improvement is to put pairs onto the min-tracker Stack. The first value of the pair would be the same as 
# before, and the second value would be how many times that minimum was repeated.


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [] 

    def push(self, val: int) -> None:
        
        # We always put the number onto the main stack.
        self.stack.append(val)
        
        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
            
        # Else if this number is equal to what's currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:

        # If the top of min stack is the same as the top of stack
        # then we need to decrement the count at the top by 1.
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1
            
        # If the count at the top of min stack is now 0, then remove
        # that value as we're done with it.
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
            
        # And like before, pop the top of the main stack.
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]


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