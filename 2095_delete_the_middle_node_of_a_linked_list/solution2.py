# Approach 2: Fast and Slow Pointers
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/solution/

# Intuition:
# The key of this approach is that we have two pointers fast and slow traversing the linked list at the same time, 
# and fast traverses twice as fast as slow. Therefore, when fast reaches the end of the linked list, slow is right 
# in the middle! We only need one iteration to reach the middle node!

# Algorithm:
# 1.If there is only one node, return null.
# 2.Otherwise, initialize two pointers slow and fast, with slow pointing to head and fast pointing to the second 
#   successor node of head.
# 3.While neither fast and fast.next is null:
#   -   we move fast forward by 2 nodes.
#   -   we move slow forward by 1 node.
# 4.Now slow is the predecessor of the middle node, delete the middle node.
# 5.Return head.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        # Edge case: return None if there is only one node.
        if head.next == None:
            return None
        
        count = 0
        p1 = p2 = head
        
        # First pass, count the number of nodes in the linked list using 'p1'.
        while p1:
            count += 1
            p1 = p1.next
        
        # Get the index of the node to be deleted.
        middle_index = count // 2
        
        # Second pass, let 'p2' move toward the predecessor of the middle node.
        for _ in range(middle_index - 1):
            p2 = p2.next
        
        # Delete the middle node and return 'head'.
        p2.next = p2.next.next
        return head


head = [1,3,4,7,1,2,6]
obj = Solution()
print(obj.deleteMiddle(head))


# Complexity Analysis:
# Let n be the length of the input linked list.
# Time complexity : O(n). 
# - We stop the iteration when the pointer fast reaches the end, fast moves forward 2 nodes per step, so there are 
#   at most n/2 steps.
# - In each step, we move both fast and slow, which takes a constant amount of time.
# - Removing the middle node also takes constant time.
# - In summary, the overall time complexity is O(n).
# Space complexity : O(1). We only need two pointers, thus the space complexity is O(1).