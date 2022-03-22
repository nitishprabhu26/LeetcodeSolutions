# Approach #2 (One-pass)
# Algorithm:
# We can greatly improve on the brute-force approach by keeping two indices i1 and i2 where we store the most 
# recent locations of word1 and word2. Each time we find a new occurrence of one of the words, we do not need to 
# search the entire array for the other word, since we already have the index of its most recent occurrence.

from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1
        minDistance = len(wordsDict)
        for i in range(len(wordsDict)):
            if word1 == wordsDict[i]:
                i1 = i
            elif word2 == wordsDict[i]:
                i2 = i
            if i1 != -1 and i2 != -1:
                minDistance = min(minDistance, abs(i1 - i2))
        return minDistance


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
obj = Solution()
print(obj.shortestDistance(wordsDict, word1, word2))


# Complexity analysis:
# Time complexity : O(N⋅M) where N is the number of words in the input list, and M is the total length of two 
# input words.
# Space complexity : O(1), since no additional space is used.
