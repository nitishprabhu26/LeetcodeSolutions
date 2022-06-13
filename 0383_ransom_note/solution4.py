# Approach 4: Sorting and Stacks
# [better than Approach 1, but worse than Approach 2 and 3]

# Intuition
# Start by converting each string into an Array of characters, and then reverse sorting them by alphabetical order. 
# It's not actually necessary to reverse sort, but it will make things easier for the rest of the algorithm.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # Reverse sort the note and magazine. In Python, we simply 
        # treat a list as a stack.
        ransomNote = sorted(ransomNote, reverse=True) 
        magazine = sorted(magazine, reverse=True)

        # While there are letters left on both stacks:
        while ransomNote and magazine:
            # If the tops are the same, pop both because we have found a match.
            if ransomNote[-1] == magazine[-1]:
                ransomNote.pop()
                magazine.pop()
            # If magazine's top is earlier in the alphabet, we should remove that 
            # character of magazine as we definitely won't need that letter.
            elif magazine[-1] < ransomNote[-1]:
                magazine.pop()
            # Otherwise, it's impossible for top of ransomNote to be in magazine.
            else:
                return False   
        # Return true iff the entire ransomNote was built.
        # if ransomNote is empty, we return True. else False
        return not ransomNote
        

ransomNote = "aa"
magazine = "aab"

obj = Solution()
print(obj.canConstruct(ransomNote, magazine))


# Complexity Analysis:
# We'll say m is the length of the magazine, and n is the length of the ransom note.
# Time Complexity : O(m.log m).
# When m < n, we immediately return false. Therefore, the worst case occurs when m ≥ n.
# Sorting the magazine is O(m.log m). Inserting the contents into the stack is O(m), which is insignificant. This, 
# therefore, gives us O(m.log m) for creating the magazine stack.
# Likewise, creating the ransom note stack is O(n.log n).
# In total, the stacks contain n + m characters. For each iteration of the loop, we are either immediately 
# returning false, or removing at least one character from the stacks. This means that the stack processing loop 
# has to use at most O(n + m) time.
# This gives us O(m.log m) + O(n.log n) + O(n + m). Now, remembering that m ≥ n it simplifies down to 
# O(m.log m) + O(m.log m) + O(m + m) = 2.O(m.log m) + O(m + m) = O(m.log m)
# Space Complexity : O(m).
# The magazine stack requires O(m) space, and the ransom note stack requires O(n) space. Because m ≥ n, this 
# simplifies down to O(m).