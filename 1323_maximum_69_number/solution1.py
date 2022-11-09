# After observation, we can get these conclusions as follows:
# - We can only increment num by converting a digit 6 to 9.
# - We should always convert the highest digit 6. Suppose num = 669, it has multiple digits 6, we must convert the 
#   first one to make it 969 rather than 699.
# - If every digit of num is 9, we only need to return num since it already stands for the largest integer.


# Approach 1: Convert the integer to an iterable object

# Intuition:
# The most intuitive method to find the first digit 6 is to traverse through each digit of num from high to low, 
# as we discussed above.
# However, we can't traverse over an integer in C++, Java, or Python, nor can we modify it. Hence, we can first 
# convert it to an iterable and mutable object, such as a string in C++, a string builder in Java, or a list in 
# Python, and traverse over the object to locate the first occurrence of 6.

# Algorithm:
# - Convert the input integer num to an iterable and mutable object num_obj.
# - Iterate over num_obj, if we find a digit 6, replace it with 9 and stop the iteration.
# - Return the integer converted from the modified num_obj.


class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert the input 'num' to a list of character 'num_char_list'.
        num_char_list = list(str(num))
        
        # Iterate over the list (from high to low).
        for i, cur_char in enumerate(num_char_list):
            # If we find the first '6', replace it with '9' and break the loop.
            if cur_char == '6':
                num_char_list[i] = '9'
                break
        
        # Convert the modified char list to integer and return it.
        return int("".join(num_char_list))
        
        
num = 9669
obj = Solution()
print(obj.maximum69Number(num))


# Complexity Analysis:
# Let L be the maximum number of digits nums can have.
# Time complexity : O(L).
# Since the input number num has up to most L digits, it requires O(L) time to convert it to an equivalent object 
# and vice versa.
# Space complexity : O(L).
# We create an object of length L.