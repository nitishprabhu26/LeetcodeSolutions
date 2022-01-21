# The obvious brute force solution is to pick all possible starting and ending positions for a substring, 
# and verify if it is a palindrome.

# Complexity Analysis:
# Time complexity : O(n^3). 
# Assume that n is the length of the input string, there are a total of n^2 such substrings (excluding the 
# trivial solution where a character itself is a palindrome). 
# Since verifying each substring takes O(n) time, the run time complexity is O(n^3).
# Space complexity : O(1).


# https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/