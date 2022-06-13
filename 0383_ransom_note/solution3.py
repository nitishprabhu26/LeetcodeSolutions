# Approach 3: One HashMap

# Intuition
# In the previous approach, we used two HashMaps. You might have noticed a slightly better way though; we can 
# simply put the magazine into a HashMap, and then subtract characters from the ransom note from it.


import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # In Python, we can use the Counter class. It does all the work that the
        # makeCountsMap(...) function in our pseudocode did!
        letters = collections.Counter(magazine)

        # For each character, c, in the ransom note:
        for c in ransomNote:
            # If there are none of c left, return False.
            if letters[c] <= 0:
                return False
            # Remove one of c from the Counter.
            letters[c] -= 1
        # If we got this far, we can successfully build the note.
        return True
        

ransomNote = "aa"
magazine = "aab"

obj = Solution()
print(obj.canConstruct(ransomNote, magazine))


# Complexity Analysis:
# We'll say m is the length of the magazine, and n is the length of the ransom note.
# Also, let k be the number of unique characters across both the ransom note and magazine. While this is never 
# more than 26, we'll treat it as a variable for a more accurate complexity analysis.
# Time Complexity : O(m).
# When m < n, we immediately return false. Therefore, the worst case occurs when m ≥ n.
# Creating a HashMap of counts for the magazine is O(m), as each insertion/ count update is is O(1), and is done 
# for each of the m characters.
# We then iterate over the ransom note, performing an O(1) operation for each character in it. This has a cost of 
# O(n).
# Becuase we know that m ≥ n, again this simplifies to O(m).
# Space Complexity : O(k) / O(1).
# We build one HashMap of counts; up to k characters in them. This means that they take up O(k) space.
# For this problem, because k is never more than 26, which is a constant, it'd be reasonable to say that this 
# algorithm requires O(1) space.