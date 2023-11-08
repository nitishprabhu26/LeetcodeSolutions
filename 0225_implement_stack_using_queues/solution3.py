# Approach #3 (One Queue, push - O(n), pop O(1))
# OR
# Neetcode: https://youtu.be/rW4vm0-DLYc?si=JpP60GQaiNX2--fK


import collections
class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


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
# Time complexity: O(n). O(n). The algorithm dequeues n elements and enqueues n−1 elements to the q, where 
# n is the stack size. This gives 2n−1 operations.
# Space complexity: O(1).