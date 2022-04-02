# Approach 1: Compare with Reverse

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list
            
inp = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(inp))

# Complexity Analysis:
# Time complexity : O(n), in length nn of the string.
# We need to iterate thrice through the string:
# 1. When we filter out non-alphanumeric characters, and convert the remaining characters to lower-case.
# 2. When we reverse the string.
# 3. When we compare the original and the reversed strings.
# Each iteration runs linear in time (since each character operation completes in constant time). Thus, the 
# effective run-time complexity is linear.
# Space complexity : O(n), in length n of the string. We need O(n) additional space to stored the filtered 
# string and the reversed string.