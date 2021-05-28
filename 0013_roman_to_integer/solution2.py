# Approach 1: Left-to-Right Pass
# the simplest algorithm is to use a pointer to scan through the string, at each step deciding whether to add the 
# current symbol and go forward 1 place, or add the difference of the next 2 symbols and go forward 2 places.

class Solution:
    def romanToInt(self, s: str) -> int:
        # Let's hard-code a mapping with the value of each symbol so that we can easily look them up.
        value={'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        i=0
        while i < len(s):
            # if at least 2 symbols remaining AND value of s[i] < value of s[i + 1]:
            if i+1<len(s) and value[s[i]] < value[s[i+1]]:
                total += value[s[i+1]] - value[s[i]]
                i += 2
            else:
                total += value[s[i]]
                i+=1
        return total

s = "MCMXCIV"
obj = Solution()
print(obj.romanToInt(s))


# Complexity Analysis:
# Let n be the length of the input string (the total number of symbols in it).

# Time complexity : O(1).
# As there is a finite set of roman numerals, the maximum number possible number can be 3999, which in roman numerals
# is MMMCMXCIX. As such the time complexity is O(1).
# Your for loop will run say a maximum of 9 times which is a constant time. So code time complexity is O(1).

# If roman numerals had an arbitrary number of symbols, then the time complexity would be proportional to the length of the input,
# i.e. O(n). This is assuming that looking up the value of each symbol is O(1).

# Space complexity : O(1).
# Because only a constant number of single-value variables are used, the space complexity is O(1).