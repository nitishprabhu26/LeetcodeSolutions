# Approach 2: Reservoir Sampling - https://youtu.be/pxvXV2bPlV0
# without using extra space
# - The reservoir sampling algorithm is intended to sample k elements from an population of unknown size. 
# In our case, the k happens to be one.

# import random
# PENDING

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:

#     def __init__(self, head: ListNode):
        
#         self.range = []
#         while head:
#             self.range.append(head.val)
#             head = head.next

#     def getRandom(self) -> int:
        
#         # https://www.w3schools.com/python/module_random.asp
#         pick = int(random.random() * len(self.range))
#         return self.range[pick]


# Input
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 3, 2, 2, 3]

input = [[[1, 2, 3]], [], [], [], [], []]
obj = Solution()
print(obj.getRandom(input))

# Complexity analysis:
# Time complexity : For the init(head) function, its time complexity is O(1).
# For the getRandom() function, its time complexity is O(N) where NN is the number of elements in the input list.
# Space Complexity: O(1). The overall solution requires O(1) space complexity, since the variables we used 
# in the algorithm are of constant size, regardless the input.

