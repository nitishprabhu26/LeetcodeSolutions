# Approach 3: Dynamic Array
# https://leetcode.com/problems/design-browser-history/editorial/

# Algorithm
# 1. Initialize variables:
#    -  An array visitedURLs, to store the visited URLs.
#    -  Two pointers currURL and lastURL, to store the index of the current and last URL in our array.
# 2. Implementing visit(url) method:
#    -  Increment currURL by 1.
#    -  If there is space available at currURL index in visitedURLs we overwrite the element at this index, 
#       otherwise insert a new element at the end.
#    -  Then we mark currURL as the lastURL.
# 3. Implementing back(steps) method:
#    -  We need to go back by step URLs.
#    -  Thus, we need to move our currURL to currURL - step index if it's in bounds or 0 otherwise.
#    -  And return the element at currURL index.
# 4. Implementing forward(steps) method:
#    -  We need to go forward by step URLs.
#    -  Thus, we need to move our currURL to currURL + step index if it's less than lastURL, or lastURL 
#       otherwise.
#    -  And return the element at currURL index.


class BrowserHistory:
    def __init__(self, homepage: str):
        # 'homepage' is the first visited URL.
        self.visited_URLs = [homepage]
        self.curr_URL, self.last_URL = 0, 0

    def visit(self, url: str) -> None:
        self.curr_URL += 1
        if len(self.visited_URLs) > self.curr_URL:
            # We have enough space in our array to overwrite an old 'url' entry with new one.
            self.visited_URLs[self.curr_URL] = url
        else:
            # We have to insert a new 'url' entry at the end.
            self.visited_URLs.append(url)
        # This 'url' will be last URL if we try to go forward.
        self.last_URL = self.curr_URL

    def back(self, steps: int) -> str:
        # Move 'curr_URL' pointer in left direction.
        self.curr_URL = max(0, self.curr_URL - steps)
        return self.visited_URLs[self.curr_URL]

    def forward(self, steps: int) -> str:
        # Move 'curr_URL' pointer in right direction.
        self.curr_URL = min(self.last_URL, self.curr_URL + steps)
        return self.visited_URLs[self.curr_URL]
        

# Your BrowserHistory object will be instantiated and called as such:
homepage = 'https://www.google.com'
url1 = 'https://github.com/'
url2 = 'https://leetcode.com/'
url3 = 'https://www.youtube.com/'
obj = BrowserHistory(homepage)
obj.visit(url1)
obj.visit(url2)
obj.visit(url3)
print('After 1st: ', obj.visited_URLs[obj.curr_URL])
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