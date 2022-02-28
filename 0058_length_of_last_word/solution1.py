# Approach 1: String Index Manipulation

# Algorithm:
# - First, we would try to locate the last word, starting from the end of the string. We iterate the string in 
# reverse order, consuming the empty spaces. When we first come across a non-space character, we know that we are 
# at the last character of the last word.
# - Second, once we locate the last word. We count its length, starting from its last character.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # trim the trailing spaces
        p = len(s) - 1
        while p >= 0 and s[p] == ' ':
            p -= 1

        # compute the length of last word
        length = 0
        while p >= 0 and s[p] != ' ':
            p -= 1
            length += 1
        return length

            
s = "Hello World"
obj = Solution()
print(obj.lengthOfLastWord(s))


# Complexity:
# Time Complexity: O(N), where N is the length of the input string.
# In the worst case, the input string might contain only a single word, which implies that we would need to 
# iterate through the entire string to obtain the result.
# Space Complexity: O(1), only constant memory is consumed, regardless the input.