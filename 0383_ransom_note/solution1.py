# Approach 1: Simulation

# Intuition
# To create our ransom note, for every character we have in the note, we need to take a copy of that character out 
# of the magazine so that it can go into the note.
# If a character we need isn't in the magazine, then we should stop and return False. Otherwise, if we manage to 
# get all the characters we need to complete the note, then we should return True.

# Algorithm:
# Strings are an immutable type. This means that they can't be modified, and so don't have "insert" and "delete" 
# operations. For this reason, we instead need to repeatedly replace the magazine with a new String, that doesn't 
# have the character we wanted to remove.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # For each character, c,  in the ransom note.
        for c in ransomNote:
            # If there are none of c left in the String, return False.
            if c not in magazine:
                return False
            # Find the index of the first occurrence of c in the magazine.
            location = magazine.index(c)
            # Use splicing to make a new string with the characters 
            # before "location" (but not including), and the characters 
            #after "location". 
            magazine = magazine[:location] + magazine[location + 1:]
        # If we got this far, we can successfully build the note.
        return True
        

ransomNote = "aa"
magazine = "aab"

obj = Solution()
print(obj.canConstruct(ransomNote, magazine))


# Complexity Analysis:
# We'll say m is the length of the magazine, and n is the length of the ransom note.
# Time Complexity : O(m⋅n).
# Finding the letter we need in the magazine has a cost of O(m). This is because we need to perform a linear 
# search of the magazine. Removing the letter we need from the magazine is also O(m). This is because we need to 
# make a new string to represent it. O(m) + O(m) = O(2 ⋅ m) = O(m) because we drop constants in big-o analysis.
# So, how many times are we performing this O(m) operation? Well, we are looping through each of the n characters 
# in the ransom note and performing it once for each letter. This is a total of n times, and so we get 
# n ⋅ O(m) = O(m ⋅ n).
# Space Complexity : O(m).
# Creating a new magazine with one letter less requires auxillary space the length of the magazine; O(m).