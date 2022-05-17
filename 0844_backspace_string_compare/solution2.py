# Approach #2: Two Pointer [Accepted]

# Intuition:
# When writing a character, it may or may not be part of the final string depending on how many backspace keystrokes occur in the future.
# If instead we iterate through the string in reverse, then we will know how many backspace characters we have seen, and therefore whether 
# the result includes our character.

# Algorithm:
# Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped. If a character 
# isn't skipped, it is part of the final answer.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skipS, skipT = 0, 0
        
        while i >= 0 or j >= 0:
            
            while i >= 0:
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            
            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            
            # If two actual characters are different
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            # If expecting to compare char vs nothing
            if (i >= 0) != (j >= 0):
                return False
            
            i -= 1
            j -= 1
            
        return True
        


s = "ab#c" 
t = "ad#c"
obj = Solution()
print(obj.backspaceCompare(s, t))


# Complexity Analysis:
# Time Complexity: O(M + N), where M, N are the lengths of S and T respectively.
# Space Complexity: O(1).