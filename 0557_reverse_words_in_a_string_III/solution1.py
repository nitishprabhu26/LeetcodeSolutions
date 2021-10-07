class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = s.split(' ')

        for i, n in enumerate(string_list):
            string_list[i] = string_list[i][::-1]

        return " ".join(string_list)

        # return " ".join(i[::-1] for i in s.split())

        # first reverse the order of the words and then reverse the entire string.
        # return ' '.join(s.split()[::-1])[::-1]


s = "Let's take LeetCode contest"
obj = Solution()
print(obj.reverseWords(s))

# Complexity analysis:
# Time complexity : O(n). where n is the length of the string.
# (Dont confuse with O(n^2) since we have [::-1] within for loop
# n refers to the input String s. you're reversing substrings of s, that in total add to n.)
# Space complexity : O(n).
