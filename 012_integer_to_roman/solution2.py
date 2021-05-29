# Approach 2: Hardcode Digits
# https://leetcode.com/problems/integer-to-roman/solution/

# Algorithm:
# The cleanest way to go about it in code is to have 4 separate arrays; one for each place value. Then, extract the digits,
# look up their symbols in the relevant array, and append them all together.

class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (thousands[num//1000] + hundreds[num % 1000//100]
                + tens[num % 100//10] + ones[num % 10])


num = 444
obj = Solution()
print(obj.intToRoman(num))
