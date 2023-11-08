# Approach #2 (Two Queues, push - O(n), pop O(1))
# https://leetcode.com/problems/implement-stack-using-queues/editorial/

# Algorithm:

# Push:
# The algorithm inserts each new element to queue q2 and keep it as the top element. In case queue q1 is not 
# empty (there are elements in the stack), we remove all elements from q1 and add them to q2. In this way the 
# new inserted element (top element in the stack) will be always positioned at the front of q2. We swap q1 
# with q2 to avoid copying all elements from q2 to q1.

# Pop:
# The algorithm dequeues an element from queue q1 and keeps front element of q1 as top.


import collections

class MyStack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        self.topEle = 0

    def push(self, x: int) -> None:
        self.q2.append(x)
        self.topEle = x
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self) -> int:
        popEle = self.q1.popleft()
        if self.q1:
            self.topEle = self.q1[0]
        return popEle

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
# Time complexity: O(n). The algorithm removes n elements from q1 and inserts n+1 elements to q2, where n is 
# the stack size. This gives 2n+1 operations. The operations add and remove in linked lists has O(1) complexity.
# Space complexity: O(1).
# Pop:
# Time complexity: O(1).
# Space complexity: O(1).