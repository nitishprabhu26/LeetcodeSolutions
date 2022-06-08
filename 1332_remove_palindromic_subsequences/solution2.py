# Approach 2: Palindrome Check with Two-Pointer Technique

# Intuition:
# The approach above solved the problem, but it required O(n) space. Another way of checking whether or not a 
# string is a palindrome is to use the two-pointer technique.

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s):
            lo = 0
            hi = len(s) - 1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        if not s:
            return 0
        if is_palindrome(s):
            return 1
        return 2


s = "baabb"
obj = Solution()
print(obj.removePalindromeSub(s))


# Complexity Analysis:
# Let n be the length of the input string.
# Time complexity : O(n).
# The loop in the isPalindrome(...) function loops up to n/2 times, each time checking whether or not the 
# characters at indexes hi and lo are equal. The division by 2 is treated as a constant so removed, and we're 
# left with O(n).
# Space complexity : O(1).
# We aren't creating any new data structures or string copies, so the total memory usage is O(1).