# Approach extra: Swapping actual nodes
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained

# Here, the very first step will be to find the K-th first and K-th last nodes.
# While doing so, we also need to store the addresses of previous nodes of the K-th first and K-th last nodes in 
# two poiners.
# left = Kth node of the Linked List
# pre_left = the previous node to left
# right = Kth node of the LinkedList from the end
# pre_right = the previous node to right


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = pre_right = pre_left = ListNode(next=head)
        right = left = head
        
        for _ in range(1, k):
            pre_left = left
            left = left.next
        
        currentNode = left

        # until we reach end of linked list
        while currentNode.next:
            pre_right = right
            right = right.next
            currentNode = currentNode.next
        
        # swapping not needed in this case
        if left == right:
            return head

        # Node swapping
        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next
        
        return dummy.next


head = [1,2,3,4,5]
k = 2
obj = Solution()
print(obj.swapNodes(head, k))


# Complexity Analysis:
# Time complexity : O(N) where N is the length of the Linked List. We are iterating over the Linked List once.
# Space complexity : O(1), as we are using constant extra space to maintain list node pointers.