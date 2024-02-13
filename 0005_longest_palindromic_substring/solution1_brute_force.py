# Approach 1 : Brute force
# The obvious brute force solution is to pick all possible starting and ending positions for a substring, 
# and verify if it is a palindrome.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(checkStr):
            if checkStr == checkStr[::-1]:
                return True
            return False

        res = s[0]
        resLen = 1
        
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if checkPalindrome(s[i : j + 1]):
                    if resLen < len(s[i : j + 1]):
                        res = s[i : j + 1]
                        resLen = len(s[i : j + 1])
                        
        return res


s = "babad"
obj = Solution()
print(obj.longestPalindrome(s))
    

# Complexity Analysis:
# Time complexity : O(n^3). 
# Assume that n is the length of the input string, there are a total of n^2 such substrings (excluding the 
# trivial solution where a character itself is a palindrome). 
# Since verifying each substring takes O(n) time, the run time complexity is O(n^3).
# Space complexity : O(1).


# https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/



# basic palindrom using 2 pointers
# def is_palindrome(s, left, right):
#     # Base case: if the pointers meet or cross each other, it's a palindrome
#     if left >= right:
#         return True
    
#     # Check if characters at the current pointers are equal
#     if s[left] != s[right]:
#         return False

#     # Move the pointers towards each other and continue the recursion
#     return is_palindrome(s, left + 1, right - 1)

# def check_palindrome(input_string):
#     # Convert the string to lowercase to make it case-insensitive
#     input_string = input_string.lower()

#     # Initialize pointers
#     left_pointer = 0
#     right_pointer = len(input_string) - 1

#     # Call the recursive function
#     return is_palindrome(input_string, left_pointer, right_pointer)

# # Example usage:
# input_str = "A man, a plan, a canal, Panama"
# result = check_palindrome(input_str)

# if result:
#     print(f'The string "{input_str}" is a palindrome.')
# else:
#     print(f'The string "{input_str}" is not a palindrome.')
