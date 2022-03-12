# Approach 3: Single Pass Approach
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/solution/

# We could use a trick to find the position of the pointer endNode in a single pass. The trick is:
# If endNode is k positions behind a certain node currentNode, when currentNode reaches the end of linked list 
# i.e at n^th node , the endNode would be at the (n-k)^th node.

# Algorithm:
# The problem can be implemented in a single pass using the following steps:
# - Start iterating from the head of the Linked List until the end using a pointer currentNode.
# - Keep track of the number of nodes traversed so far using the variable listLength. The listLength is incremented 
#   by 1 as each node is traversed.
# - If listLength is equal to k, we know that currentNode is pointing to the k^th node from the beginning. Set 
#   frontNode to point to the k^th node. Also, at this point, initialize endNode to point at the head of the 
#   linked list. Now we know that endNode is k nodes behind the head node.
# - If endNode is not null, we know that it is positioned k nodes behind the currentNode and so we increment 
#   endNode in addition to currentNode. When currentNode reaches the end of the list, endNode would be pointing 
#   at a node which is k nodes behind the last node.
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
        endNode = None
        currentNode = head
        
        # set the front node and end node in single pass
        while currentNode:
            listLength += 1
            if endNode:
                endNode = endNode.next
            # check if we have reached kth node
            if listLength == k:
                frontNode = currentNode
                endNode = head
            currentNode = currentNode.next
        
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
# Time complexity : O(N) where N is the length of the Linked List. We are iterating over the Linked List once.
# Space complexity : O(1), as we are using constant extra space to maintain list node pointers frontNode, endNode 
# and currentNode.