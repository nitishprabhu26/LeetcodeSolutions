# Approach: 
# https://www.youtube.com/watch?v=urzP1YbgUnU


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        

head = [4,5,1,9]
node = 5
obj = Solution()
print(obj.deleteNode(node))


# Complexity analysis:
# Time complexity : O(1).
# Space complexity : O(1).