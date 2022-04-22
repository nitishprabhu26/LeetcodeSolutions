# Approach 2: Recursive (Advanced)
# https://leetcode.com/problems/palindrome-linked-list/solution/

# Algorithm:
# When given the head node (or any other node), referred to as currentNode, the algorithm firstly checks the rest 
# of the Linked List. If it discovers that further down that the Linked List is not a palindrome, then it returns 
# false. Otherwise, it checks that currentNode.val == frontPointer.val. If not, then it returns false. Otherwise, 
# it moves frontPointer forward by 1 node and returns true to say that from this point forward, the Linked List is 
# a valid palindrome.
# It might initially seem surprisingly that frontPointer is always pointing where we want it. The reason it works 
# is because the order in which nodes are processed by the recursion is in reverse . Each node compares itself 
# against frontPointer and then moves frontPointer down by 1, ready for the next node in the recursion. In essence,
# we are iterating both backwards and forwards at the same time.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


# Complexity analysis:
# Time complexity : O(n), where n is the number of nodes in the Linked List.
# Space complexity : O(n), where n is the number of nodes in the Linked List. O(n) is used for recursive stack.

# Not only is this approach still using O(n) space, it is worse than the first approach because in many languages 
# (such as Python), stack frames are large, and there's a maximum runtime stack depth of 1000 (you can increase it,
# but you risk causing memory errors with the underlying interpreter). With every node creating a stack frame, this
# will greatly limit the maximum Linked List size the algorithm can handle.