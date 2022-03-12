# Approach 1: Three Pass Approach
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/solution/

# Algorithm:
# We must implement the algorithm using 3 separate passes.
# Pass 1: Find the length of the Linked List by traversing each node in the list from head node to last node and 
#         increment the counter by 1. Let the counter used to find length be listLength.
# Pass 2: Traverse until the k^th node from the head node and set the frontNode
# Pass 3: Traverse until the listLength - k node from the head node and set the endNode.
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
        
        # find the length of linked list
        while currentNode:
            listLength += 1
            currentNode = currentNode.next
            
        # set the front node at kth node
        frontNode = head
        for i in range(1, k):
            frontNode = frontNode.next
        
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
# Time complexity : O(N) where N is the length of the Linked List. We are iterating over the Linked List thrice.
# Space complexity : O(1), as we are using constant extra space to maintain list node pointers frontNode, endNode 
# and currentNode.