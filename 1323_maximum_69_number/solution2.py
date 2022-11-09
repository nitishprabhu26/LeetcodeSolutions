# Approach 2: Use built-in function

# Algorithm:
# - Convert the input number num to the string num_string.
# - Use the built-in function to replace the first 6 to 9 if it exists.
# - Return the integer converted from the modified num_string.

# https://www.geeksforgeeks.org/python-string-replace/


class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert the input 'num' to the string 'num_string'.
        num_string = str(num)

        # Use the built-in function to replace the first '6' with '9'.
        # Return the integer converted from the modified 'num_string'.
        return int(num_string.replace('6', '9', 1))
        
        
num = 9669
obj = Solution()
print(obj.maximum69Number(num))


# Complexity Analysis:
# Let L be the maximum number of digits nums can have.
# Time complexity : O(L).
# We need to look for the first occurrence of digit 6 and make at most one replacement, which takes O(L) time.
# Space complexity : O(L).
# We convert num to a string of length L, therefore, the space complexity is O(L).