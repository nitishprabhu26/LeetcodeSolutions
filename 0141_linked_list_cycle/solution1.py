# Approach 1: Hash Table

# Algorithm
# We go through each node one by one and record each node's reference (or memory address) in a hash table. 
# If the current node is null, we have reached the end of the list and it must not be cyclic. If current 
# node’s reference is in the hash table, then return true.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_seen = set()
        while head:
            if head in node_seen:
                return True
            node_seen.add(head)
            head = head.next
        return False

head = [3,2,0,-4]
obj = Solution()
print(obj.hasCycle(head))

# Complexity analysis
# Let n be the total number of nodes in the linked list.
# Time complexity : O(n). We visit each of the n elements in the list at most once. Adding a node to the hash 
# table costs only O(1) time.
# Space complexity: O(n). The space depends on the number of elements added to the hash table, which contains 
# at most n elements.