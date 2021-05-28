# Approach 3: Right-to-Left Pass
# we can process one symbol each time we go around the main loop. We still need to determine whether or not our current symbol 
# should be added or subtracted by looking at the neighbour though.

class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Let's hard-code a mapping with the value of each symbol so that we can easily look them up.
        values={'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        total = values.get(s[-1])
        # for i in range(len(s)-2,-1,-1):
        for i in reversed(range(len(s)-1)):
            if values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
        
s = "MCMXCIV"
obj = Solution()
print(obj.romanToInt(s))