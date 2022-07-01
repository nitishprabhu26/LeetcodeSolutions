# https://leetcode.com/problems/strobogrammatic-number/solution/
# 8, 0, and 1 are themselves upside-down. 6 and 9 are each other upside-down. All other numbers, including 2 and 5, 
# are not themselves up-side-down, nor are they any other number up-side-down.
 
 
# Approach 1: Make a Rotated Copy
# Intuition:
# A straightforward solution is to make a copy of the input that is rotated by 180 degrees. If the rotated copy is 
# identical to the original input, then the input has to be strobogrammatic.

# Algorithm:
# Recall that when a number is rotated by 180 degrees, the order of the digits reverses and each digit is rotated 
# upside-down in its new position. As such, we could build a new rotated string by looping through the original 
# string backward (to reverse it) and rotating + appending each digit to the new string.
# Recall from above that the rules for rotating a character are as follows:
# 0 ⟶ 0
# 1 ⟶ 1
# 6 ⟶ 9
# 8 ⟶ 8
# 9 ⟶ 6
# The digits 2, 3, 4, 5, and 7 are not rotatable. Their presence immediately signifies that the input number 
# couldn't possibly be rotatable, and therefore not strobogrammatic.


# 1. The simplest way of doing the rotations in code is to use if statements.
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        # In Python, we use a list as a string builder.
        rotated_string_builder = []
        
        # Remember that we want to loop backward through the string.
        for c in reversed(num):
            if c in {'0', '1', '8'}:
                rotated_string_builder.append(c)
            elif c == '6':
                rotated_string_builder.append('9')
            elif c == '9':
                rotated_string_builder.append('6')
            else: # This must be an invalid digit.
                return False
        
        # In Python, we convert a list of characters to
        # a string using join.
        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num


# 2. Alternatively, you could use a hash map, or even an array, to store the rules for flipping.
# 2a. Here is the code using a Hash Map to avoid the need for a complex conditional statement.
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        rotated_string_builder = []
        
        for c in reversed(num):
            if c not in rotated_digits:
                return False
            rotated_string_builder.append(rotated_digits[c])
        
        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num


# 2b. Alternatively, we could use an Array instead of a Hash Map; the indexes act as keys.
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        rotated_digits = ['0', '1', '', '', '', '', '9', '', '8', '6']
        
        rotated_string_builder = []
        
        for c in reversed(num):
            rotated_string_builder.append(rotated_digits[int(c)])
        
        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num


num = "69"
obj = Solution()
print(obj.isStrobogrammatic(num))


# Complexity analysis:
# Let N be the length of the input string.
# Time complexity : O(N)
# In the worst case, all digits in the string will be rotatable. We're going to assume this for the time complexity 
# analysis. 
# For each of the N digits in the string, we're looking up (with a hash map, array, or cascading if) the rotation 
# of that digit. For all three sub-implementations, this has a cost of O(1). 
# Appending to the end of a string builder is also O(1). 
# Therefore, building the 180-degree rotation of a string has a cost of O(N).
# In the final step, we're comparing two strings of length N. This also has a cost of O(N).
# This gives us O(N) + O(N). In Big-O notation, we treat this as simply O(N).
# Space complexity : O(N). The string builder requires O(N) space.

# Note that if you didn't implement your string building sensibly (e.g., if you used string concatenation), then 
# your solution will have a time complexity of O(N^2).