# Approach 2: Two Pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


inp = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(inp))


# Complexity Analysis:

# Time complexity : O(n), in length nn of the string. We traverse over each character at-most once, until the two pointers meet in the middle, or when we break and return early.
# Space complexity : O(1). No extra space required, at all.
