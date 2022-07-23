# Approach 2: Iterative Link Reversal.

# Intuition:
# In the previous approach, we looked at an algorithm for reversing a portion of the given linked list such that 
# the underlying structure doesn't change. We only modified the values of the nodes for achieving the reversal. 
# However, it may so happen that you cannot change the data available in the nodes. In that scenario, we have to 
# modify the links themselves to achieve the reversal.
# Essentially, starting from the node at position m and all the way up to n, we reverse the next pointers for all 
# the nodes in between.

# Algorithm:
# 1. We need two pointers, prev and cur.
# 2. The prev pointer should be initialized to None initially, while cur is initialized to the head of the linked 
#    list.
# 3. We progress the cur pointer one step at a time and the prev pointer follows it.
# 4. We keep progressing the two pointers in this way until the cur pointer reaches the m^{th} node from the 
#    beginning of the list. This is the point from where we start reversing our linked list.
# 5. An important thing to note here is the usage of two additional pointers which we will call as tail and con. 
#    The tail pointer points to the m^{th} node from the beginning of the linked list and we call it a tail pointer
#    since this node becomes the tail of the reverse sublist. The con points to the node one before m^{th} node and 
#    this connects to the new head of the reversed sublist.
# 6. The tail and the con pointers are set once initially and then used in the end to finish the linked list 
#    reversal.
# 7. Once we reach the m^{th} node, we iteratively reverse the links as explained before using the two pointers. 
#    We keep on doing this until we are done reversing the link (next pointer) for the n^{th} node. At that point, 
#    the prev pointer would point to the n^{th} node.
# 8. We use the con pointer to attach to the prev pointer since the node now pointed to by the prev pointer (the 
#    n^{th} node from the beginning) will come in place of the m^{th} node due after the reversal. Similarly, we 
#    will make use of the tail pointer to connect to the node next to the prev node i.e. (n+1)^{th} node from the 
#    beginning.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head


head = [1,2,3,4,5]
left = 2
right = 4
obj = Solution()
print(obj.reverseBetween(head, left, right))


# Complexity Analysis:
# Time Complexity: O(N) considering the list consists of N nodes. We process each of the nodes at most once 
# (we don't process the nodes after the n^{th} node from the beginning.
# Space Complexity: O(1) since we simply adjust some pointers in the original linked list and only use O(1) 
# additional memory for achieving the final result.