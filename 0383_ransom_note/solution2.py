# Approach 2: Two HashMaps

# Intuition
# Count up how many of each letter are in both the magazine and the ransom note. We can represent the counts with 
# a HashMap that has characters as keys, and counts as values.


import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # In Python, we can use the Counter class. It does all the work that the
        # makeCountsMap(...) function in our pseudocode did!
        magazine_counts = collections.Counter(magazine)
        ransom_note_counts = collections.Counter(ransomNote)

        # For each *unique* character in the ransom note:
        for char, count in ransom_note_counts.items():
            # Check that the count of char in the magazine is equal
            # or higher than the count in the ransom note.
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False

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
# Likewise, creating the HashMap of counts for the ransom note is O(n).
# We then iterate over the ransom note HashMap, which contains at most n unique values, looking up their 
# counterparts in the magazine `HashMap. This is, therefore, at worst O(n).
# This gives us O(n) + O(n) + O(m). Now, remember how we said m ≥ n? This means that we can simplify it to 
# O(m) + O(m) + O(m) = 3.O(m) = O(m), dropping the constant of 3.
# Space Complexity : O(k) / O(1).
# We build two HashMaps of counts; each with up to k characters in them. This means that they take up O(k) space.
# For this problem, because k is never more than 26, which is a constant, it'd be reasonable to say that this 
# algorithm requires O(1) space.