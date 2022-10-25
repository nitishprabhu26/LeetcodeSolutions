# Approach 2: Two Pointers
# OR
# https://youtu.be/GT_bL44OdwQ

# Intuition:
# If we observe closely, we can notice that we need to compare each character at corresponding positions in the 
# two arrays. Also, this comparison needs to be continuous over the strings in the array.
# We can keep two pointers, one pointing to the first character of the first string in the array 'word1' and the 
# other pointing to the first character of the first string in the array 'word2'. Then we will compare the 
# characters at these indices and can return false if they aren't the same, otherwise, we will increment both 
# pointers. Now it might be possible that after incrementing the pointers, one or both of them have exhausted the 
# whole string and are now pointing to the non-existing indices. We need to move to the next string in the array 
# in such cases. Hence we need to have two more pointers that will be pointing to the strings in the two array 
# lists.

# Algorithm:
# 1.Initialize 'word1Pointer' and 'word2Pointer' to 0. These pointers will be pointing to the current string in the 
#   array word1 and word2 respectively.
# 2.Initialize 'string1Pointer' and 'string2Pointer' to 0. These pointers will be pointing to the current characters 
#   in the strings pointed by the above two pointers.
# 3.While we still have strings to iterate over in both the lists:
#   -   If the character at 'string1Pointer' in the string at index 'word1Pointer' in the list 'word1' isn't equal 
#       to the character at 'string2Pointer' in the string at index 'word2Pointer' in the list 'word2', then return 
#       false. Otherwise, increment both the string pointers i.e., 'string1Pointer' and 'string2Pointer' to check 
#       the next characters.
#   -   If the pointer 'string1Pointer' has reached the end of string then reset it to zero and increment the word 
#       pointer 'word1Pointer'.
#   -   If the pointer 'string2Pointer' has reached the end of string then reset it to zero and increment the word 
#       pointer 'word2Pointer'.
# 4.Return true if the 'word1Pointer' and 'word2Pointer' has reached the end of array. This is important as it 
#   might happen that one of the list has no more strings but the other one still has some and in that case we 
#   must return false.


from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Pointers to mark the current word in the given two lists.
        word1Pointer, word2Pointer = 0, 0
        
        # Pointers to mark the character in the string pointed by the above pointers.
        string1Pointer, string2Pointer = 0, 0
        
        # While we still have the string in any of the two given lists.
        while word1Pointer < len(word1) and word2Pointer < len(word2):
            
            # If the characters at the two string are same, increment the string pointers
            # Otherwise return false.
            if word1[word1Pointer][string1Pointer] != word2[word2Pointer][string2Pointer]:
                return False
            string1Pointer += 1
            string2Pointer += 1

            # If the string pointer reaches the end of string in the list word1,
            # Move to the next string in the list and, reset the string pointer to 0.
            if string1Pointer == len(word1[word1Pointer]):
                word1Pointer += 1
                string1Pointer = 0
            
            # If the string pointer reaches the end of string in the list word2,
            # Move to the next string in the list and, reset the string pointer to 0.
            if string2Pointer == len(word2[word2Pointer]):
                word2Pointer += 1
                string2Pointer = 0
                
        # Strings in both the lists should be traversed.
        return word1Pointer == len(word1) and word2Pointer == len(word2)
        

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