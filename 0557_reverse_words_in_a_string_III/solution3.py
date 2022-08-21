# Approach 1: Traverse and Reverse each character one by one

# Algorithm:
# - Find the starting and ending position of each word in the string.
# - For each identified word, reverse the characters of the word one by one.


class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        lastSpaceIndex = -1
        s_len = len(s)
        
        for strIndex in range(0, s_len):
            if strIndex == (s_len - 1) or s[strIndex] == " ":
                reverseStrIndex = strIndex if (strIndex == s_len - 1) else strIndex - 1

                for index in range(reverseStrIndex, lastSpaceIndex, -1):
                    res += s[index]
                
                if strIndex != s_len - 1:
                    res += ' '
                
                lastSpaceIndex = strIndex
        
        return res


s = "Let's take LeetCode contest"
obj = Solution()
print(obj.reverseWords(s))


# Complexity analysis:
# Let N be the length of input string s.
# Time complexity : O(N) Every character in the string is traversed twice. First, to find the end of the current 
# word, and second to reverse the word and append it to the result. Thus the time complexity is, O(N + N) = O(N).
# Space complexity : O(1) We use constant extra space to track the last space index.
