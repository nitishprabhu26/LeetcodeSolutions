# Approach : converting to integers and mapping pattern
# https://youtu.be/nIAJF5r4z2M


from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def get_pattern(s):
            lookup = {}
            output = []
            i = 0
            for c in s:
                if c in lookup:
                    output.append(lookup[c])
                else:
                    i += 1
                    lookup[c] = i
                    output.append(i)
            return output

        p = get_pattern(pattern)
        result = []
        for word in words:
            if get_pattern(word) == p:
                result.append(word)
        return result


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
obj = Solution()
print(obj.findAndReplacePattern(words, pattern))


# Complexity Analysis
# Time Complexity: O(N * K), where N is the number of words, and K is the length of each word.
