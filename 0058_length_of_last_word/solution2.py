# Approach 2: One-loop Iteration

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p, length = len(s), 0

        while p > 0:
            p -= 1
            # we're in the middle of the last word
            if s[p] != ' ':
                length += 1
            # here is the end of last word
            elif length > 0:
                return length

        return length

# OR (p-initialized and p-decrement placed differently)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p, length = len(s)-1, 0

        while p >= 0:
            # we're in the middle of the last word
            if s[p] != ' ':
                length += 1
            # here is the end of last word
            elif length > 0:
                return length
            p -= 1

        return length


s = "Hello World"
obj = Solution()
print(obj.lengthOfLastWord(s))


# Complexity:
# Time Complexity: O(N), where N is the length of the input string.
# This approach has the same time complexity as the previous approach. The only difference is that we combined 
# two loops into one.
# Space Complexity: O(1), only constant memory is consumed, regardless the input.
