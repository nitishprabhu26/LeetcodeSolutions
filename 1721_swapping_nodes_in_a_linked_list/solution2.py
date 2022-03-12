# Approach 2: Two Pass Approach
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/solution/

# Algorithm:
# The problem can be solved in two passes with the following steps:
# - Iterate from the head of the Linked List until the end and store the length found in listLength. In the same 
#   loop, check if we have reached the k^th node, and if so, set frontNode to point at that node.
# - Iterate from head node until listLength - k node and set the endNode.
# - Swap the values of frontNode and endNode using temporary variable temp.
# - Return the head node.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listLength = 0
        currentNode = head
        
        # find the length of list and set the front node
        while currentNode:
            listLength += 1
            if listLength == k:
                frontNode = currentNode
            currentNode = currentNode.next
            
        # set the end node at (listLength - k)th node
        endNode = head
        for i in range(1, listLength - k + 1):
            endNode = endNode.next
        
        # swap the values of front node and end node
        temp = frontNode.val
        frontNode.val = endNode.val
        endNode.val = temp
        
        return head


head = [1,2,3,4,5]
k = 2
obj = Solution()
print(obj.swapNodes(head, k))


# Complexity Analysis:
# Time complexity : O(N) where N is the length of the Linked List. We are iterating over the Linked List twice.
# Space complexity : O(1), as we are using constant extra space to maintain list node pointers frontNode, endNode 
# and currentNode.