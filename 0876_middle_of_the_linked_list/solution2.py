# Approach 1: Output to Array

# Algorithm:
# Put every node into an array A in order. Then the middle node is just A[A.length // 2], since we can retrieve 
# each node by index.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while head.next:
            head = head.next
            arr.append(head)
        return arr[len(arr)//2]

# OR

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]


head = [1, 2, 3, 4, 5]
obj = Solution()
print(obj.middleNode(head))


# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the given list.
# Space Complexity: O(N), the space used by A.