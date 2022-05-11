# Approach 3: Bit Manipulation

# XOR concepts:.
#     0 ^ 0 = 0
#     0 ^ 1 = 1
#     1 ^ 0 = 1
#     1 ^ 1 = 0
# Look at how the similar ones just even out. When all the other similar pairs just even out or reduce to a zero, 
# the different one would remain.
# Thus, the left over bits after XORing all the characters from string s and string t would be from the extra 
# character of string t.

# Algorithm:
# - Initialize a variable ch which would hold the XORed results.
# - XOR all the characters with ch while iterating through string s.
# - XOR all the characters with ch while iterating through string t. (Alternatively, we could have also combined 
#   steps 2 and 3).
# - Return ch as the answer.


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Initialize ch with 0, because 0 ^ X = X
        # 0 when XORed with any bit would not change the bits value.
        ch = 0

        # XOR all the characters of both s and t.
        for char_ in s:
            ch ^= ord(char_)

        for char_ in t:
            ch ^= ord(char_)

        # What is left after XORing everything is the difference.
        return chr(ch)


# OR
# take the difference of ord sum

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_ord, t_ord = 0, 0
        for ss in s:
            s_ord += ord(ss)
        for tt in t:
            t_ord += ord(tt)

        return chr(t_ord - s_ord)


s = "abcd"
t = "abcde"
obj = Solution()
print(obj.findTheDifference(s, t))


# Complexity Analysis:
# Time complexity: O(N), where N is length of the strings. Since, we iterate through both the strings once.
# Space complexity: O(1).