# Approach 1: Fixed-Range Sampling
# One of the most intuitive ideas would be that we convert the linked list into an array. With the array, 
# we would know its size and moreover we could have an instant access to its elements.

import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: ListNode):
        
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        
        # https://www.w3schools.com/python/module_random.asp
        pick = int(random.random() * len(self.range))
        return self.range[pick]


# Input
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 3, 2, 2, 3]

input = [[[1, 2, 3]], [], [], [], [], []]
obj = Solution()
print(obj.getRandom(input))

# Complexity analysis:
# Time complexity : O(N) where N is the number of elements in the linked list. 
# For the getRandom() function, its time complexity is O(1).
# Space complexity : The overall solution requires O(N) space complexity, since we make a copy of elements 
# from the input list.

