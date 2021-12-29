# Approach 2: Floyd's Cycle Finding Algorithm

# Algorithm:
# The space complexity can be reduced to O(1) by considering two pointers at different speed - a slow
# pointer and a fast pointer. The slow pointer moves one step at a time while the fast pointer moves two
# steps at a time.
# If there is no cycle in the list, the fast pointer will eventually reach the end and we can return
# false in this case.
# else fast pointer will eventually meet slow pointer because fast is faster


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True


head = [3, 2, 0, -4]
obj = Solution()
print(obj.hasCycle(head))

# Complexity analysis
# Let n be the total number of nodes in the linked list.
# Time complexity : O(n).
# To analyze its time complexity, we consider the following two cases separately:
# -- List has no cycle:
# The fast pointer reaches the end first and the run time depends on the list's length, which is O(n).
# -- List has a cycle:
# fast pointer will eventually meet slow pointer because fast is faster. gap could possibly be entire length
# of the linkedlist. i.e. to bring 10 down to 0.
# Space complexity: O(1). We only use two nodes (slow and fast)
