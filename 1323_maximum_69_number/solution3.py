# Approach 3: Check the remainder
# https://leetcode.com/problems/maximum-69-number/solution/

# Intuition:
# Can we locate the highest digit of 6 without converting num to string? The answer is Yes!
# We can always get the last digit of a non-negative integer by taking the remainder of num divided by 10, 
# for example, to get the last digit of 613:
# 613 % 10 = 3

# How about the second last digit?
# We can 'remove' the last digit by taking the quotient of num and 10.
# 613 / 10 = 61
# Therefore, we can check every digit of num from low to high and record the highest digit 6. 

# Assume that it is the k-th digit (0 based), 'converting' this digit from 6 to 9 equals adding 3⋅10^k 
# to the original integer num.

# Algorithm:
# 1.Initialize an integer num_copy = num for checking digits.
# 2.Get the remainder of num_copy and 10.
# 3.If the remainder is 6, record the current digit as the first (highest) digit of 6.
# 4.Divide num_copy by 10 using integer division.
# - If num_copy = 0, go to step 5.
# - Otherwise, repeat step 2.
# 5.If we find the first digit of 6, let's say index_first_six, increment num by 3.10^index_first_six
#   and return num. Otherwise, just return num.


class Solution:
    def maximum69Number (self, num: int) -> int:
        # Since we start with the lowest digit, initialize curr_digit = 0.
        curr_digit = 0
        index_first_six = -1
        num_copy = num
        
        # Check every digit of 'num_copy' from low to high.
        while num_copy:
            # If the current digit is '6', record it as the highest digit of 6.
            if num_copy % 10 == 6:
                index_first_six = curr_digit
            
            # Move on to the next digit.
            num_copy //= 10
            curr_digit += 1
        
        # If we don't find any digit of '6', return the original number,
        # otherwise, increment 'num' by the difference made by the first '6'.
        return num if index_first_six == -1 else num + 3 * 10 ** index_first_six
        
        
num = 9669
obj = Solution()
print(obj.maximum69Number(num))


# Complexity Analysis:
# Let L be the maximum number of digits nums can have.
# Time complexity : O(L).
# We need to make at most L time of integer divisions, which takes O(L) time.
# Space complexity : O(1).
# We only need to update several variables, which takes O(1) space.