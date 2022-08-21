# Approach 2: Using Two Pointers

# Intuition:
# In the previous approach, the words were reversed by copying every character into another string one by one in 
# reverse order. This operation takes O(N) time, where N is the length of the word.
# However, there is another optimal approach to reverse the string in O(N/2) time in place using two pointer 
# approach.
# In this solution, we will traverse the string and find every word's start and end index. Then, we will reverse 
# each word using the two-pointer approach.

# Algorithm:
# - The variable lastSpaceIndex stores the index of space character last found. Initialize its value to -1.
# - Traverse over each character of the string from 0^{th} index to n^{th} index using pointer strIndex.
# - As strIndex points to a space character, mark the start and end index of the current word in the variables 
#   startIndex and endIndex as,
#   -   The startIndex of the current word is the value of lastSpaceIndex + 1.
#   -   The endIndex of the current word is the value of strIndex - 1.
# - Reverse the characters in the current word using two pointer approach.
# - Update the lastSpaceIndex to the value of strIndex i.e the index of current space character. The next iteration 
#   will refer to this variable to identify the start position of the next word.
# - Repeat the process for all the words in the string.


class Solution:
    def reverseWords(self, s: str) -> str:
        chArray = list(s)
        lastSpaceIndex = -1
        s_len = len(s)
        
        for strIndex in range(0, s_len + 1):
            if strIndex == s_len or chArray[strIndex] == " ":
                startIndex = lastSpaceIndex + 1
                endIndex = strIndex - 1
                
                while startIndex < endIndex:
                    chArray[startIndex], chArray[endIndex] = chArray[endIndex], chArray[startIndex]
                    startIndex += 1
                    endIndex -= 1
                
                lastSpaceIndex = strIndex
        
        return ''.join(chArray)


s = "Let's take LeetCode contest"
obj = Solution()
print(obj.reverseWords(s))


# Complexity analysis:
# Let N be the length of input string s.
# Time complexity : O(N) The outer loop iterates over N characters to find the start and end index of every word. 
# The algorithm to reverse the word also iterates N times to perform N/2 swaps. Thus, the time complexity is 
# O(N + N) = O(N).
# Space complexity : O(1) We use constant extra space to track the last space index.
