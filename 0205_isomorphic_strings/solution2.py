# Approach 2: First occurence transformation

# Intuition:
# This approach is based on the idea that the two given strings, if isomorphic, will in some way be exactly the 
# same. If we have two isomorphic strings, we can replace the characters in the first string with the corresponding 
# mapped characters to get the second string. The idea we explore here is the following:
# Is there any string transformation we can apply to both the strings such that to check for isomorphism, we simply 
# check if their modified versions are exactly the same?
# For each character in the given string, we replace it with the index of that character's first occurence in the 
# string.
# eg: For strings like paper and title, the transformed strings will be 01034.
# However, we should be mindful of transformations that use both one and two-digit numbers. Under these 
# circumstances, the transformed strings can be misinterpreted.
# To avoid confusion, we can add a delimiter to help differentiate the transformed digits. Thus, by adding spaces 
# we obtain 
# stenographics = 0 1 2 3 4 5 6 7 8 9 10 11 0 and 
# logarithmsxox = 0 1 2 3 4 5 6 7 8 9 10 1 10. 
# As a side note, this issue can also be resolved by comparing arrays of the transformed digits instead of using 
# strings.


# Algorithm:
# 1. Define a function called transform that takes a string as an input and returns a new string with modifications 
# as explained in the intuition section.
#    a. We maintain a dictionary to store the character to index mapping for the given string.
#    b. For each character, we look up the mapping in the dictionary. If there is a mapping, that means this 
#       character already has its first occurrence recorded and we simply use the first occurrence's index in the 
#       new string. Otherwise, we use the current index for the first occurrence.
# 2. We find the transformed strings for both of our input strings, s1 and s2 respectively.
# 3. If s1 == s2, that implies the two input strings are isomorphic. Otherwise, they're not.


class Solution:
    
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))
        
        return " ".join(new_str)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)


s = "egg"
t = "add"
obj = Solution()
print(obj.isIsomorphic(s, t))


# Complexity analysis:
# Here N is the length of each string (if the strings are not the same length, then they cannot be isomorphic).
# Time Complexity: O(N). We process each character in both the strings exactly once to determine if the strings 
# are isomorphic.
# Space Complexity: O(N). We form two new strings returned by our transformation function i.e. O(N).
# The size of ASCII character set is fixed and the keys in our dictionary are valid ASCII characters only. So the 
# size of the map in the transform function doesn't contribute to the space complexity.