# In this problem, we are given a linked list head and the task is to remove the middle node.
# We are also given the definition of middle node. Suppose there are n nodes in the linked list, then the index of 
# the middle node middleIndex is: middleIndex = floor(n / 2) - 1, if we use 0-base indexing.

# Approach 1: 2 Passes

# Intuition:
# We make the first iteration, starting from head, goint through the entire linked list and getting the total 
# number of nodes (let's say count). According to the definition provided, the index of the middle node is 
# middleIndex = floor(count / 2) - 1.
# Now we make a second iteration to the predecessor node of the middle node, which means that we stop at index 
# middleIndex - 1.
# Once we reach the predecessor node of the middle node, we can remove the middle node from the linked list.

# Algorithm:
# - If there is only one node, return null.
# - Otherwise, initialize two pointers p1 = head and p2 = head.
# - Iterate the linked list with p1 and count the total number of nodes it has (count).
# - Let p2 move forward by floor(count / 2) - 1 nodes, now it is the predecessor of the middle node, delete the 
#   middle node.
# - Return head.


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
        # OR use while loop instead of above for loop
        # while middle_index - 1 > 0:
        #     p2 = p2.next
        #     middle_index -= 1

        # Delete the middle node and return 'head'.
        p2.next = p2.next.next
        return head


head = [1,3,4,7,1,2,6]
obj = Solution()
print(obj.deleteMiddle(head))


# Complexity Analysis:
# Let n be the length of the input linked list.
# Time complexity : O(n). 
# - We iterate over the linked list twice, the first time traversing the entire linked list and the second 
#   traversing half of it. Hence there are a total of O(n) steps.
# - In each step, we move a pointer forward by one node, which takes constant time.
# - Remove the middle node takes a constant amount of time.
# - In summary, the overall time complexity is O(n).
# Space complexity : O(1). We only need two pointers, thus the space complexity is O(1).