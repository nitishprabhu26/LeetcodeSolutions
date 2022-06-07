# Approach 2: Hash Table

# Intuition:
# Approach 1 is inefficient because we repeatedly traverse over list B to check whether or not any of the nodes in 
# list B were equal to the current one we were looking at in list A. Instead of repeatedly traversing through 
# list B though, we could simply traverse it once and store each node in a hash table. We could then traverse 
# through list A once, each time checking whether the current node exists in the hash table.

# Algorithm:
# Traverse list B and store the address/reference of each node in a hash table. Then for each node in list A, 
# check whether or not that node exists in the hash table. If it does, return it as it must be the intersection 
# node. If we get to the end of list A without finding an intersection node, return null.
# The one thing we need to be careful of is that we're comparing objects of type Node. We don't want to compare 
# the values within the nodes; doing this would cause our code to break when two different nodes have the same 
# value.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None


# Complexity Analysis:
# Let N be the length of list A and M be the length of list B.
# Time Complexity : O(N + M).
# Firstly, we need to build up the hash table. It costs O(1) to insert an item into a hash table, and we need to 
# do this for each of the M nodes in list B. This gives a cost of O(M) for building the hash table.
# Secondly, we need to traverse list A, and for each node, we need to check whether or not it is in the hash table.
# In the worst case, there will not be a match, requiring us to check all N nodes in list A. As it is also O(1) 
# to check whether or not an item is in a hash table, this checking has a total cost of O(N).
# Finally, combining the two parts, we get O(M) + O(N) = O(M + N).
# Space Complexity : O(M).
# As we are storing each of the nodes from list B into a hash table, the hash table will require O(M) space. Note 
# that we could have instead stored the nodes of list A into the hash table, this would have been a space 
# complexity of O(N). Unless we know which list is longer though, it doesn't make any real difference.