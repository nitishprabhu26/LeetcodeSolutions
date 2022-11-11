# Approach 2: Doubly Linked List
# https://leetcode.com/problems/design-linked-list/solution/

# Time to implement DLL MyLinkedList, which is a much faster (twice faster on the testcase set here) though a bit 
# more complex. It contains size, sentinel head and sentinel tail.
# Note, that sentinel head and tail are always present.

# Add at Index, Add at Head and Add at Tail:
# The idea is simple:
# - Find the predecessor and the successor of the node to insert. If the node is to be inserted at head, its 
#   predecessor is a sentinel head. If the node is to be inserted at tail, its successor is a sentinel tail. 
#   (Use bidirectional search to perform faster).
# - Insert the node by changing the links to the next and previous nodes.
# to_add.prev = pred
# to_add.next = succ
# pred.next = to_add
# succ.prev = to_add

# Delete at Index:
# Basically, the same as insert:
# - Find the predecessor and successor.
# - Delete node by changing the links to the next and previous nodes.
# pred.next = succ
# succ.prev = pred

# Get:
# Get is very straightforward:
# - Compare index and size - index to define the fastest way: starting from the head, or starting from the tail.
# - Go to the wanted node.
# # choose the fastest way: to move from the head
# # or to move from the tail
# if index + 1 < self.size - index:
#     curr = self.head
#     for _ in range(index + 1):
#         curr = curr.next
# else:
#     curr = self.tail
#     for _ in range(self.size - index):
#         curr = curr.prev


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        # choose the fastest way: to move from the head
        # or to move from the tail
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
                
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node 
        will be the first node of the linked list.
        """
        pred, succ = self.head, self.head.next
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        succ, pred = self.tail, self.tail.prev
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of 
        linked list, the node will be appended to the end of linked list. If index is greater than the length, the 
        node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        # find predecessor and successor of the node to be added
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        
        # insertion itself
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
            
        # delete pred.next 
        self.size -= 1
        pred.next = succ
        succ.prev = pred


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
# Time complexity : O(1) for addAtHead and addAtTail. O(min(k, N−k)) for get, addAtIndex, and deleteAtIndex, where 
# k is an index of the element to get, add or delete.
# Space complexity : O(1) for all operations.
