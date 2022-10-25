# Approach 1: Concatenate and Compare

# Intuition:
# In this approach, we will do as the problem says. We will find the string represented by each array and then 
# check if the two strings are equal or not. To find the string represented by the array, we just need to append 
# all the strings present in it to one another in the same order they are present in the array.

# Algorithm:
# - Iterate over strings present in the array word1, append each string to a string word1Combined.
# - Iterate over strings present in the array word2, append each string to a string word2Combined.
# - Compare the above strings and return true if both are the same, otherwise return false.

# The string object in Python is immutable, which means every time a string is assigned to a variable, a new object 
# is created in the memory to describe a new value. StringBuilder objects are like String objects, except that they 
# can be modified. StringBuilder class in Java is also used to create mutable string objects.
# Note: In Java, we must use StringBuilder, as strings are Immutable in Java.


from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Creates a new string by combining all the strings in word1.
        word1Combined = ""
        for s in word1:
            word1Combined += s
        
        # Creates a new string by combining all the strings in word2.
        word2Combined = ""
        for s in word2:
            word2Combined += s
        
        # Returns true if both string are the same.
        return word1Combined == word2Combined


# OR
# Using the join() method in python
        
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
        

word1 = ["ab", "c"]
word2 = ["a", "bc"]
obj = Solution()
print(obj.arrayStringsAreEqual(word1, word2))


# Complexity Analysis:
# Here N is the number of strings in the list and K is the maximum length of a string in it.
# Time Complexity: O(N * K).
# - We iterate over each string in the arrays to append them. This cost us O(N * K) as we traversed over each 
#   character of the string to perform an append operation.
# - In the end, the comparison between the two strings also takes O(N * K) time.
# - Hence, the total time complexity is equal to O(N * K).
# Space complexity : O(N * K).
# We need to have two strings to store the strings represented by the arrays. Therefore, the total space 
# complexity is equal to O(N * K).