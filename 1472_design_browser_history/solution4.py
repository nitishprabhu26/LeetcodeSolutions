# Approach : Using arrays (same as Approach 3: Dynamic Array)
# Neetcode: https://youtu.be/i1G-kKnBu8k?si=S4Un-tmPpd2tlS9b

class BrowserHistory:
    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.len - 1, self.i + steps)
        return self.history[self.i]
        

# Your BrowserHistory object will be instantiated and called as such:
homepage = 'https://www.google.com'
url1 = 'https://github.com/'
url2 = 'https://leetcode.com/'
url3 = 'https://www.youtube.com/'
obj = BrowserHistory(homepage)
obj.visit(url1)
obj.visit(url2)
obj.visit(url3)
print('After 1st: ', obj.history[obj.i])
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
#   -   In the visit(url) method, we insert the URL string in our array and update the current pointer, both of 
#       these operations will take O(1) time each.
#       Thus, in the worst case each call to the visit(url) method will take O(1) time.
#   -   In the back(steps) and forward(steps) methods, we directly return the element at the required index 
#       which takes O(1) time.
#       Thus, in the worst case, each call to these methods will take O(1) time.
# Space complexity:
#   -   We might visit n URL strings and they will be stored in our array.
#   -   Thus, in the worse case, we use O(l⋅n) space.