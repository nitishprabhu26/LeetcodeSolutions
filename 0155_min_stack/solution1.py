# https://leetcode.com/problems/min-stack/solution/

# We're told that all the MinStack operations must run in constant time, i.e. O(1) time. For this reason, we can 
# immediately rule out the use of a Binary Search Tree or Heap. While these data structures are often great for 
# keeping track of a minimum, their core operations (find, add, and remove) are O(logn), which isn't good enough.


# Approach 1: Stack of Value/ Minimum Pairs:

# Recall that with a Stack, we only ever add (push) and remove (pop) numbers from the top. Therefore, an 
# important invariant of a Stack is that when a new number, which we'll call x, is placed on a Stack, the 
# numbers below it will not change for as long as number x remains on the Stack. Numbers could come and go 
# above x for the duration of x's presence, but never below.

# So, whenever number x is the top of the Stack, the minimum will always be the same, as it's simply the minimum 
# out of x and all the numbers below it.

# Therefore, in addition to putting a number on an underlying Stack inside our MinStack, we could also put its 
# corresponding minimum value alongside it. Then whenever that particular number is at the top of the underlying 
# Stack, the getTop(...) operation of MinStack is as simple as retrieving its corresponding minimum value.


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self.stack:
            self.stack.append((val, val))
            return
        
        current_min = self.stack[-1][1]
        self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


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
# Let n be the total number of operations performed.
# Time Complexity : O(1) for all operations.
# Space Complexity : O(n).
# Worst case is that all the operations are push. In this case, there will be O(2⋅n) = O(n) space used.