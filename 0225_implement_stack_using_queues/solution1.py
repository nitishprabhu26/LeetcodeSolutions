# Approach #1 (Two Queues, push - O(1), pop O(n))
# https://leetcode.com/problems/implement-stack-using-queues/editorial/

# Intuition:
# Stack is LIFO (last in - first out) data structure, in which elements are added and removed from the same end, 
# called top.
# In general stack is implemented using array or linked list, but in the current article we will review a 
# different approach for implementing stack using queues. In contrast queue is FIFO (first in - first out) data 
# structure, in which elements are added only from the one side - rear and removed from the other - front. 
# In order to implement stack using queues, we need to maintain two queues q1 and q2. Also we will keep top 
# stack element in a constant memory.

# Algorithm:

# Push:
# The new element is always added to the rear(right side) of queue q1 and it is kept as top stack element

# Pop:
# We need to remove the element from the top of the stack. This is the last inserted element in q1.
# Because queue is FIFO (first in - first out) data structure, the last inserted element could be removed only 
# after all elements, except it, have been removed. For this reason we need to maintain additional queue q2, 
# which will serve as a temporary storage to enqueue the removed elements from q1. The last inserted element in 
# q2 is kept as top. Then the algorithm removes the last element in q1. 
# We swap q1 with q2 to avoid copying all elements from q2 to q1.


import collections

class MyStack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        self.topEle = 0
        
    def push(self, x: int) -> None:
        self.q1.append(x)
        self.topEle = x

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.topEle = self.q1.popleft()
            self.q2.append(self.topEle)
        popElement = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return popElement

    def top(self) -> int:
        return self.topEle

    def empty(self) -> bool:
        return len(self.q1) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
print('Top: ', obj.top())
print('Pop: ', obj.pop())
print('Top: ', obj.top())
print('isEmpty: ', obj.empty())


# Complexity Analysis:
# Push:
# Time complexity: O(1).
# Space complexity: O(1).
# Pop:
# Time complexity: O(n). O(n). The algorithm dequeues n elements from q1 and enqueues n−1 elements to q2, where 
# n is the stack size. This gives 2n−1 operations.
# Space complexity: O(1).