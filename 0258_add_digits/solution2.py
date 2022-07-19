# Approach 1: Mathematical: Digital Root
# https://leetcode.com/problems/add-digits/solution/
# OR
# https://youtu.be/doTBRB6_IFs

# "The original number is divisible by 9 if and only if the sum of its digits is divisible by 9."

# There is a known formula to compute a digital root in a decimal numeral system:
# To consider separately three cases: 
# - the sum of digits is 0:
#   dr_{10}(n) = 0,   if n = 0
# - the sum of digits is divisible by 9:
#   dr_{10}(n) = 9,   if n = 9k
# - the sum of digits is not divisible by nine:
#   dr_{10}(n) = n,   if n != 9k


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

        
num = 38
obj = Solution()
print(obj.addDigits(num))


# Complexity Analysis:
# Time Complexity: O(1).
# Space Complexity: O(1).