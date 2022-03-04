# Approach : bit manipulation
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/discuss/1164135/Simple-solution-no-setmap 
# (check comments for explaination)

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        occurred = 0
        for i in sentence:
            temp = ord(i) - ord('a')
            # here << is bitwise left-shift operator which will shift the 1st bit of 1 to left by temp places.
            occurred |= (1 << temp)
            # print(bin(occurred))
        # return true if all alphabet have occurred atleast once
        if occurred == (1 << 26) - 1:
            return True
        return False

sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "leetcode"
obj = Solution()
print(obj.checkIfPangram(sentence))


# Complexity Analysis:
# Time complexity: O(n).
# Space complexity: O(1).