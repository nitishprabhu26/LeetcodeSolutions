# Approach : Neetcode
# https://youtu.be/KT9rltZTybQ

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            i -= 1
            length += 1

        return length


s = "Hello World"
obj = Solution()
print(obj.lengthOfLastWord(s))


# Complexity:
# Time Complexity: O(N), where N is the length of the input string.
# Space Complexity: O(1), only constant memory is consumed, regardless the input.
