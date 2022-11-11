# Overview:
# Singly linked list is the simplest one, it provides addAtHead in a constant time, and addAtTail in a linear time. 
# Though doubly linked list is the most used one, because it provides both addAtHead and addAtTail in a constant 
# time, and optimises the insert and delete operations.

# Sentinel nodes are widely used in the trees and linked lists as pseudo-heads, pseudo-tails, etc. They serve as 
# the guardians, as the name suggests, and usually they do not hold any data.
# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/


# Approach 1: Singly Linked List
# https://leetcode.com/problems/design-linked-list/solution/

# Note, that sentinel node is used as a pseudo-head and is always present. This way the structure could never be 
# empty, it will contain at least a sentinel head. 

# Add at Index, Add at Head and Add at Tail:
# Let's first discuss insert at index operation, because thanks to the sentinel node addAtTail and addAtHead 
# operations could be reduced to this operation as well.
# The idea is straightforward:
# - Find the predecessor of the node to insert. If the node is to be inserted at head, its predecessor is a 
#   sentinel head. If the node is to be inserted at tail, its predecessor is the last node.
# - Insert the node by changing the link to the next node.
# to_add.next = pred.next
# pred.next = to_add

# Delete at Index
# Basically, the same as insert:
# - Find the predecessor.
# - Delete node by changing the links to the next node.
# # delete pred.next 
# pred.next = pred.next.next

# Get
# Get is a very straightforward: start from the sentinel node and do index + 1 steps
# # index steps needed 
# # to move from sentinel node to wanted index
# for _ in range(index + 1):
#     curr = curr.next
# return curr.val


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node 
        will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of 
        linked list, the node will be appended to the end of linked list. If index is greater than the length, 
        the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

# Adding values to Linked List
obj.addAtHead(1)
obj.addAtHead(2)
obj.addAtTail(3)
obj.addAtIndex(1,8)

# Print all values of linked List after adding all elements
curr = obj.head
linkListStr = ""
while curr:
    linkListStr += str(curr.val) + " -> "
    curr = curr.next
print("Linked List after adding all elements: ",linkListStr)

param_1 = obj.get(0)
print("Get the 0-th index element of Linked List: ", param_1)

# Print all values of linked List after deleting an element at index 2
obj.deleteAtIndex(2)
curr = obj.head
linkListStr = ""
while curr:
    linkListStr += str(curr.val) + " -> "
    curr = curr.next
print("Linked List after deleting an element at index '2': ",linkListStr)


# Complexity Analysis:
# Time complexity : O(1) for addAtHead. O(k) for get, addAtIndex, and deleteAtIndex, where k is an index of the 
# element to get, add or delete. O(N) for addAtTail.
# Space complexity : O(1) for all operations.
