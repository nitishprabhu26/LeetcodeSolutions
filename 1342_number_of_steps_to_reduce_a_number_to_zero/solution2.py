# Approach 2: Counting Bits
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/solution/

# Intuition:
# At each step, we either subtract 1 from num, or we divide num by 2. 
# - Odd numbers always have a last bit of 1. Subtracting 1, from an odd number, changes the last bit from 1 to 0.
# - Dividing by 2 removes the last bit from the number.
# Check example. The bits slid along, and each became the "last" bit. Notice how the 0s took one step to remove, 
# and the 1s took two steps to remove.
# So, to get our answer, we can just add two steps for every 1, and add one step for every 0, for each bit in 
# the binary representation.
# There's one thing to be careful of, and that is not inadvertently counting the last bit as two steps. The last 
# bit to remove will always be a 1 — it was the most significant bit in the original num. The algorithm above 
# would add 2 for removing this final 1. But actually, when we subtract 1 from it, it goes to zero. So we don't 
# need add two steps for this bit. The simplest way of handling this case is to subtract 1 from our final steps 
# count, as we know this "off-by-one-error" will always happen (except when the initial num is 0, we need to be 
# careful of that edge case too!).

# Algorithm:
# To count the bits we'll convert our number into a binary string, for each character if it's a "1" we'll add two 
# steps, else if it's "0" we'll add one step.
# In Java, we can use Integer.toBinaryString(...) to convert an int to binary. The binary number is represented as 
# String.
# In Python, we can use bin(...) to convert an int to binary. Like in Java, the binary number is represented as a 
# str. However, it also contains 0b on the start—this is simply a code to say the str is a binary number. The 
# "pythonic" thing to do is chop these two characters off with a list splice. i.e., to get the binary for num, you 
# would do bin(num)[2:].


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        # Get the binary for num, as a String. Remove the "0b" off the start with splice.
        binary = bin(num)[2:]

        # Iterate over all the bits in the binary string.
        for bit in binary:
            # Must use "1", not 1 here. The bits are strings!
            if bit == "1": # If the bit is a 1 
                steps = steps + 2 # Then it'll take 2 to remove.
            else: # bit == "0"
                steps = steps + 1 # Then it'll take 1 to remove.

        # We need to subtract 1, because the last bit was over-counted.
        return steps - 1


# OR
# In Python, we can do this really elegantly using the string.count(...) and len(...) functions.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary = bin(num)[2:]
        ones = binary.count("1")
        total = len(binary)
        return ones + total - 1


num = 14
obj = Solution()
print(obj.numberOfSteps(num))


# Complexity Analysis:
# Let n = num.
# Time complexity : O(log n).
# Converting a number into string can be done in O(log n) time.
# We then loop over each bit, doing a single operation each time. The number of bits in a number is log_2(number), 
# so the time complexity is O(log n).
# Space complexity : O(log n).
# Because we convert the number into a string, we'll have log_2(number) characters in our string. This gives us a 
# space complexity of O(log n).