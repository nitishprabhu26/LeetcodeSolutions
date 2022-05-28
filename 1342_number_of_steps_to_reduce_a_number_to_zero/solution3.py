# Approach 3: Counting Bits with Bitwise Operators

# In Approach 2, we needed to convert the number into a string representation. Strings are considerably larger 
# than the integer they represent though. Another way of inspecting bits, to check if they're 1 or 0, is to use 
# the bitwise-and (&) operator.
# The result of a & b (a bitwise-and b) looks at each bit in both a and b at the same time. If both bits are 1 
# then bitwise-and sets the same bit of the result to 1, but if either are 0 it sets the bit to 0.

# So, to actually inspect a specific bit, we can use a number that has a 1 followed by enough 0s to put the 1 at 
# the position we want it (we commonly call this a "bitmask"). With this number, we bitwise-and (&) it with the 
# input number. If the input number has a 1 at the same position, it'll output 1 at that position, and because all 
# other numbers are 0 they will be 0 in the output as well.
# These numbers of the form 1, followed by some number of 0s, are actually just the powers of two, where the power 
# is the number of 0s after the one. As such, we can check if a bit is a 1 in a number by doing num & (1 << bit) 
# where bit is the bit we want to check (0-indexed from the right).
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/solution/
# Just like Approach 2, we look at each bit, and if it's a 1 we add 2 to steps, otherwise if it's a 0, we add 1 
# to steps.

# Algorithm:
# Unlike the previous approach, this approach won't work correctly when num = 0 is the input. The previous approach
# did an iteration for the lone 0 bit as it was in the string, but for this approach the loop won't run at all. -1 
# will then be returned because of the steps - 1. The solution is to check for num == 0 at the start and return 0 
# if it is detected.


class Solution:
    def numberOfSteps(self, num: int) -> int:

        # We need to handle this as a special case, otherwise it'll return -1.
        if num == 0: return 0

        steps = 0
        power_of_two = 1

        while power_of_two <= num:
            # Apply the bit mask to check if the bit at "power_of_two" is a 1.
            if (power_of_two & num) != 0:
                steps = steps + 2
            else:
                steps = steps + 1
            power_of_two = power_of_two * 2

        # We need to subtract 1, because the last bit was over-counted.
        return steps - 1


num = 14
obj = Solution()
print(obj.numberOfSteps(num))


# Complexity Analysis:
# Let n = num.
# Time complexity : O(log n).
# We're pulling out each of the logn bits from num and performing an O(1) operation on each one. Therefore, the 
# total time complexity is O(logn).
# Space complexity : O(1).
# We only use a constant number of integer variables, and so the space complexity is O(1).