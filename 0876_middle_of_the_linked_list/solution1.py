# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid_node = head
        last_node = 0
        while head.next:
            head = head.next
            if last_node % 2 == 0:
                mid_node = mid_node.next
            last_node += 1
        return mid_node


head = [1, 2, 3, 4, 5]
obj = Solution()
print(obj.middleNode(head))
