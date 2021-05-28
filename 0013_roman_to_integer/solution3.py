# Approach 2: Left-to-Right Pass Improved:
# Instead of viewing a Roman Numeral as having 7 unique symbols, we could instead view it as having 13 unique symbols
# — some of length-1 and some of length-2.

class Solution:
    def romanToInt(self, s: str) -> int:
        # Let's hard-code a mapping with the value of each symbol so that we can easily look them up.
        values={'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        total = 0
        i=0

        while i < len(s):
            # if at least 2 symbols remaining AND s.substing(i, i + 1) is in values:
            # or s[slice(i,i+2)]
            if i+1<len(s) and s[i:i+2] in values:
                total += values.get(s[i:i+2])
                i += 2
            else:
                total += values.get(s[i:i+1])
                i+=1
        return total

s = "MCMXCIV"
obj = Solution()
print(obj.romanToInt(s))


# Complexity Analysis:

# Time complexity : O(1).
# Same as Approach 1.

# Space complexity : O(1).
# Same as Approach 1.