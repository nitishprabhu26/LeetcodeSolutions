# Approach 2: Doubly Linked List
# https://leetcode.com/problems/design-browser-history/editorial/
# OR
# Neetcode: https://youtu.be/i1G-kKnBu8k?si=IjUU-sCxKflYMdfo


# Algorithm
# 1. Create a class DLLNode for each node of the doubly linked list:
#    -  It contains a string variable data to store the URL string.
#    -  And two pointers prev and next pointing to the rest of the doubly linked list.
# 2. In the BrowserHistory class, we create two variables:
#    -  linkedListHead, points to the head of our doubly linked list and is storing the homepage URL.
#    -  current, it will always point to the current URL node in our doubly linked list.
# 3. Implementing visit(url) method:
#    -  We create a new node for url.
#    -  Make our current node's next point to this new node and the new node's prev point to the current node. 
#       Thus, deleting the link of the next nodes of current and inserting the new node in our doubly linked 
#       list.
#    -  Then, mark this new node as the current node.
# 4. Implementing back(steps) method:
#    -  We will move the current pointer towards the left (using prev pointer) in the doubly linked list if 
#       nodes are present and the step number of nodes is not traversed.
#    -  At the end, we return the current node's URL.
# 5. Implementing forward(steps) method:
#    -  We will move the current pointer towards the right (using next pointer) in the doubly linked list if 
#       nodes are present and the step number of nodes is not traversed.
#    -  At the end, we return the current node's URL.


class DLLNode:
    def __init__(self, url: str):
        self.data = url
        self.prev, self.next = None, None

class BrowserHistory:
    def __init__(self, homepage: str):
        # 'homepage' is the first visited URL.
        self.linked_list_head = DLLNode(homepage)
        self.current = self.linked_list_head

    def visit(self, url: str) -> None:
        # Insert new node 'url' in the right of current node.
        new_node = DLLNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        # Make this new node as current node now.
        self.current = new_node

    def back(self, steps: int) -> str:
        # Move 'current' pointer in left direction.
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.data

    def forward(self, steps: int) -> str:
        # Move 'current' pointer in right direction.
        while steps and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.data
        

# Your BrowserHistory object will be instantiated and called as such:
homepage = 'https://www.google.com'
url1 = 'https://github.com/'
url2 = 'https://leetcode.com/'
url3 = 'https://www.youtube.com/'
obj = BrowserHistory(homepage)
obj.visit(url1)
obj.visit(url2)
obj.visit(url3)
print('After 1st: ', obj.current.data)
param_2 = obj.back(1)
print('After 2nd: ', param_2)
param_3 = obj.back(1)
print('After 3rd: ', param_3)
param_4 = obj.forward(3)
print('After 4th: ', param_4)


# Complexity Analysis:
# Let's assume here, n visit calls are made, m is the maximum number of steps to go forward or back, and l is 
# the maximum length of the URL string.
# Time complexity: 
#   -   In the visit(url) method, we insert a new node in our doubly linked list, it will take O(l) time to 
#       create a new node (to allocate memory for l characters of the url string), and then we mark this new 
#       node as current which will take O(1) time.
#       Thus, in the worst case each call to the visit(url) method will take O(l) time.
#   -   In the back(steps) and forward(steps) methods, we iterate on our doubly linked list nodes and stop when 
#       m nodes are iterated or we reached the end.
#       Thus, in the worst case, each call to these methods will take O(min⁡(m,n)) time.
# Space complexity:
#   -   We might visit n URL strings and they will be stored in our doubly linked list.
#   -   Thus, in the worse case, we use O(l⋅n) space.