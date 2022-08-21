# Two-pointer approach (without split())

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        l, r = 0, 0
        while r < len(s):
            if s[r] != " ":
                r += 1
            else:
                res += s[l:r+1][::-1]
                r += 1
                l = r

        # Once the loop ends, we have the last word unprocessed.
        # Need to add it manually.
        # adding an extra space to 'res' before reversing the last substring
        res += " "
        res += s[l:r][::-1]
        
        # res has one extra whitespace in the beginning. It appeared when we were appending the first word.
        return res[1:]


s = "Let's take LeetCode contest"
obj = Solution()
print(obj.reverseWords(s))


# Complexity analysis:
# Time complexity : O(n).
# (Dont confuse with O(n^2) since we have [::-1] within while loop
# n refers to the input String s. you're reversing substrings of s, that in total add to n.)
# Space complexity : O(n).
