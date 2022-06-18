# Approach 1: Built-in Split + Reverse
# Benefits: in-place in Python (in-place, but linear space complexity!) and the simplest one to write.


class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(s.split()[::-1])
        return " ".join(reversed(s.split()))


s = "the sky is blue"
obj = Solution()
print(obj.reverseWords(s))


# Complexity Analysis:
# Time complexity: O(N), where N is a number of characters in the input string.
# Space complexity: O(N), to store the result of split by spaces.