# Approach 2: Two Stacks

# Approach 1 required storing two values in each slot of the underlying Stack. Sometimes though, the minimum 
# values are very repetitive.
# We could instead have two Stackss inside our MinStack. The main Stack should keep track of the order numbers 
# arrived (a standard Stack), and the second Stack should keep track of the current minimum. We'll call this 
# second Stack the "min-tracker" Stack for clarity.

# The push(...) method for this implementation of MinStack is straightforward. Items should always be pushed onto 
# the main Stack, but they should only be pushed onto the min-tracker Stack if they are smaller than the current 
# top of it. 

# MinStack's two getter methods, top(...) and getMin(...) are also straightforward with this approach. top(...) 
# returns (but doesn't remove) the top value of the main Stack, whereas getMin(...) returns (but doesn't remove) 
# the top of the min-tracker Stack.

# MinStack's pop(...) method. The value we actually need to pop is always on the top of the main underlying Stack. 
# However, if we simply popped it from there, the min-tracker Stack would become incorrect once its top value had 
# been removed from the main Stack.

# A logical solution would be to do the following additional check and modification to the min-tracker Stack when 
# MinStack's pop(...) method is called.

# If top of main_stack == top of min_tracker_stack:
#     min_tracker_stack.pop()
# This way, the new minimum would now be the top of the min-tracker Stack.


# One more condition for pitfall:
# While 6 was already at the top of the min-tracker Stack, we pushed another 6 onto the MinStack. Because this 
# new 6 was equal to the current minimum, it didn't change what the current minimum was, and therefore wasn't 
# pushed. At first, this worked okay.

# The problem occurred though when we started calling pop(...) on MinStack. When the most recent 6 was pop'ed, 
# the condition for popping the min-tracker Stack too was triggered (i.e. that both internal stacks have the same 
# top). This isn't what we wanted though—it was the earlier 6 that triggered the push(...) onto the min-tracker 
# Stack, not the latter one! The 6 should have been left alone with that first pop(...).

# Instead of only pushing numbers to the min-tracker Stack if they are less than the current minimum, we should 
# push them if they are less than or equal to it. While this means that some duplicates are added to the 
# min-tracker Stack, the bug will no longer occur. Check animation

from typing import List

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if an element equal to the current minimum is added again (2nd condition in OR):
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



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