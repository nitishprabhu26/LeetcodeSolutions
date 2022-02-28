# Approach 3: Built-in String Functions

# In Python, we would use the following built-in functions to accomplish the tasks:
# str.isspace(): this function determines if the str contains only spaces.
# str.split(delimiter): this function could split the input string into several substrings, based on the given 
# delimiter (by default, the delimiter is space).

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if not s or s.isspace() else len(s.split()[-1])

# OR

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split().pop())

# OR

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = "Hello World"
obj = Solution()
print(obj.lengthOfLastWord(s))


# Complexity:
# Time Complexity: O(N), where N is the length of the input string.
# It would be safe to assume the time complexity of the methods such as str.split() and String.lastIndexOf() to 
# be O(N), since in the worst case we would need to scan the entire string for both methods.
# Space Complexity: O(N). Again, we should look into the built-in functions that we used in the algorithm.
# In the Python implementation, we used str.split(), which returns a list of substrings that are separated by 
# the space delimiter. As a result, we would need O(N) space for our algorithm to store this list.
