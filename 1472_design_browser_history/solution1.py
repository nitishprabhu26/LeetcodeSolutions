# Approach 1: Two Stacks
# https://leetcode.com/problems/design-browser-history/editorial/

# Algorithm
# 1. Initialize variables:
#    -  Two stacks of strings history and future, to store the URLs.
#    -  A string variable current, to store the currently visited URL, which is initialized with the given 
#       homepage as it is the first visited URL.
# 2. Implementing visit(url) method:
#    -  As we will visit a new URL url, we will store current in the history stack, and
#    -  make the given url as current, and clear the forward stack.
# 3. Implementing back(steps) method:
#    -  We need to go back by step URLs.
#    -  While there are elements in the history stack and we haven't popped step elements from it, we will push 
#       current in the future stack and pop the most recently visited URL from the history stack and mark it as 
#       current.
#    -  At the end, we return current.
# 4. Implementing forward(steps) method:
#    -  We need to go forward by step URLs.
#    -  While there are elements in the forward stack and we haven't popped step elements from it, we will push 
#       current in the history stack and pop the most recently visited URL from the forward stack and mark it 
#       as current.
#    -  At the end, we return current.


class BrowserHistory:

    def __init__(self, homepage: str):
        self._history, self._future = [], []
        # 'homepage' is the first visited URL.
        self._current = homepage
        
    def visit(self, url: str) -> None:
        # Push 'current' in 'history' stack and mark 'url' as 'current'.
        self._history.append(self._current)
        self._current = url
        # We need to delete all entries from 'future' stack.
        self._future = []
        
    def back(self, steps: int) -> str:
        # Pop elements from 'history' stack, and push elements in 'future' stack.
        while steps > 0 and self._history:
            self._future.append(self._current)
            self._current = self._history.pop()
            steps -= 1
        return self._current        

    def forward(self, steps: int) -> str:
        # Pop elements from 'future' stack, and push elements in 'history' stack.
        while steps > 0 and self._future:
            self._history.append(self._current)
            self._current = self._future.pop()
            steps -= 1
        return self._current
        

# Your BrowserHistory object will be instantiated and called as such:
homepage = 'https://www.google.com'
url1 = 'https://github.com/'
url2 = 'https://leetcode.com/'
url3 = 'https://www.youtube.com/'
obj = BrowserHistory(homepage)
obj.visit(url1)
obj.visit(url2)
obj.visit(url3)
print('After 1st: ', obj._current)
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
#   -   In the visit(url) method, we push the URL string in the history stack, assign the given url string as 
#       the current URL, and then we clear the future stack, all these operations take O(1) time each.
#       Thus, in the worst case each call to the visit(url) method will take O(1) time.
#   -   In the back(steps) and forward(steps) methods, we push and pop strings in the future and history stacks.
#       We do these two operations unless we are done with m steps or all elements are removed from the stack 
#       which might have n elements in it.
#       Thus, in the worst case, each call to these methods will take O(min(m,n)) time.
# Space complexity:
#   -   We might visit n URL strings and they will be stored in our stacks.
#   -   Thus, in the worse case, we use O(l⋅n) space.