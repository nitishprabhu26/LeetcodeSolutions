# Three conditions must be met for the two strings to be isomorphic:
# 1. We can map a character only to itself or to one other character.
# 2. No two character should map to same character.
# 3. Replacing each character in string s with the character it is mapped to results in string t.

# Approach 1: Character Mapping with Dictionary

# We will process both of the strings from left to right. At each step, we take one character at a time from the 
# two strings and compare them. There are three cases we need to handle here:
# 1. If the characters don't have a mapping, we add one in the dictionary and move on.
# 2. The characters already have a mapping in the dictionary. If that is the case, then we're good to go.
# 3. The final case is when a mapping already exists for one of the characters but it doesn't map to the other 
#    character at hand. In this case, we can safely conclude that the given strings are not isomorphic and we can 
#    return.
# The above three cases only care about one-way-mapping i.e. mapping characters from the first string to the 
# second one only. Don't we need the mapping from the other side as well?
# We will need two dictionaries instead of one since we need one-to-one mapping from the string s to string t and 
# vice versa. Let's look at the algorithm to see the modified cases.

# Algorithm:
# 1. We define a dictionary mapping_s_t which will be used to map characters in string s to characters in string t 
#    and another dictionary mapping_t_s which will be used to map characters in string t to characters in string s.
# 2. Next, we iterate over the two strings one character at a time.
# 3. Let's assume the character in the first string is c1 and the corresponding character in second string is c2.
#    a. If c1 does not have a mapping in mapping_s_t and c2 does not have a mapping in mapping_t_s, we add the 
#       corresponding mappings in both the dictionaries and move on to the next character.
#    b. At this point, we expect both the character mappings to exist in the dictionaries and their values should 
#       be mapping_s_t[c1] = c2 and mapping_t_s[c2] = c1. If either of these conditions fails (c1 is not in the 
#       dictionary, c2 is not in the dictionary, unexpected mapping), we return false.
# 4. Return true once both the strings have been exhausted.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}
        
        for c1, c2 in zip(s, t):
            
            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            
            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both            
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
            
        return True
        

s = "egg"
t = "add"
obj = Solution()
print(obj.isIsomorphic(s, t))


# Complexity analysis:
# Here N is the length of each string (if the strings are not the same length, then they cannot be isomorphic).
# Time Complexity: O(N). We process each character in both the strings exactly once to determine if the strings 
# are isomorphic.
# Space Complexity: O(1) since the size of the ASCII character set is fixed and the keys in our dictionary are all 
# valid ASCII characters according to the problem statement.
