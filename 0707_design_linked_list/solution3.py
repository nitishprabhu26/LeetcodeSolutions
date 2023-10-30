# Neetcode: Doubly linked List
# https://youtu.be/Wf4QhpdVFQo?si=MORDFzZwvQRAupfi


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next = ListNode(val), self.left, self.left.next
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.right.prev, self.right
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        next = self.left.next
        while next and index > 0:
            next = next.next
            index -= 1
        
        if next and index == 0:
            node, prev = ListNode(val), next.prev
            node.next, node.prev = next, prev
            next.prev = node
            prev.next = node


    def deleteAtIndex(self, index: int) -> None:
        node = self.left.next
        while node and index > 0:
            node = node.next
            index -= 1
        
        if node and node != self.right and index == 0:
            node.prev.next = node.next
            node.next.prev = node.prev


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

# Adding values to Linked List
obj.addAtHead(1)
obj.addAtHead(2)
obj.addAtTail(3)
obj.addAtIndex(1,8)

# Print all values of linked List after adding all elements
curr = obj.left
linkListStr = ""
while curr:
    linkListStr += str(curr.val) + " -> "
    curr = curr.next
print("Linked List after adding all elements: ",linkListStr)

param_1 = obj.get(0)
print("Get the 0-th index element of Linked List: ", param_1)

# Print all values of linked List after deleting an element at index 2
obj.deleteAtIndex(2)
curr = obj.left
linkListStr = ""
while curr:
    linkListStr += str(curr.val) + " -> "
    curr = curr.next
print("Linked List after deleting an element at index '2': ",linkListStr)


# Complexity Analysis:
# Time complexity : O(1) for addAtHead and addAtTail. O(min(k, N−k)) for get, addAtIndex, and deleteAtIndex, where 
# k is an index of the element to get, add or delete.
# Space complexity : O(1) for all operations.
