# Approach 2: Regex

# Algorithm:

# The pattern of case 1 in regex is [A-Z]*, 
# where [A−Z] matches one char from 'A' to 'Z', 
# * represents repeat the pattern before it at least 0 times. 
# Therefore, this pattern represents "All capital".

# The pattern of case 2 in regex is [a-z]*, 
# where similarly, [a-z] matches one char from 'a' to 'z'. 
# Therefore, this pattern represents "All not capital".

# Similarly, the pattern of case 3 in regex is [A-Z][a-z]*.

# Take these three pattern together, we have [A-Z]* | [a-z]* | [A-Z][a-z]* 
# where "|" represents "or".
# Still, we can combine case 2 and case 3, and we get .[a-z]*, where "." can matches any char.

# Therefore, the final pattern is [A-Z]* | .[a-z]*

import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
        # OR - min length 1 is given
        # return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
        

# OR
# https://youtu.be/V4fhgbLsE0k

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        elif word.lower() == word:
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False


# OR

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in (
            word.upper(),
            word.lower(),
            word.capitalize(),
        )
        # OR
        # return word.islower() or word.isupper() or word.istitle()


word = "USA"
obj = Solution()
print(obj.detectCapitalUse(word))


# Complexity Analysis:
# Time complexity : O(N), but depends on implementation.
# However, it is worth pointing out that the speed of regex is highly dependent on its pattern and its 
# implementation, and the time complexity can vary from O(1) to O(2^n). If you want to control the speed 
# yourself, using Approach 1 would be better.
# Space complexity : O(1). We only need constant spaces to store our variables.
