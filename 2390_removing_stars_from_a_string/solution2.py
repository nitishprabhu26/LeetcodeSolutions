# Approach 2: Strings

# Algorithm:
# 1. Create an empty string variable answer that will store the string while performing the required operations.
# 2. Iterate over the string s from start and for each index i of the string:
#    -  If s[i] == '*', delete the last character from answer.
#    -  Otherwise, we have a non-star character, so we append it to answer.
# 3. Return answer.


class Solution:
    def removeStars(self, s: str) -> str:
        answer = ""
        for i in range(0, len(s)):
            if s[i] == '*':
                answer = answer[:-1]
            else:
                answer += s[i]

        return answer
        

s = "leet**cod*e"
obj = Solution()
print(obj.removeStars(s))


# Complexity Analysis:
# Time complexity : O(n). We iterate over s and for every character we either append it to answer or delete the 
# last character from answer which takes O(1) time per character. It takes O(n) time for n characters.
# Note: This approach does not work for Python as the strings are immutable in Python, so this would result in an
#       O(n^2) time complexity.
# Space complexity : O(n).
# The answer string can have a maximum of n characters, requiring O(n) space. Normally, we do not count the answer 
# towards the space complexity, but in this case we are performing logic on the answer variable, so we are 
# counting it.