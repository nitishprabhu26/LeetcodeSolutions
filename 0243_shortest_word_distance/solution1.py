# This is a straight-forward coding problem. The distance between any two positions i_1 and i_2 in an array is 
# |i_1 - i_2|. To find the shortest distance between word1 and word2, we need to traverse the input array and 
# find all occurrences i_1 and i_2 of the two words, and check if |i_1 - i_2| is less than the minimum distance 
# computed so far.
 
# Approach #1 (Brute Force)
# Algorithm:
# A naive solution to this problem is to go through the entire array looking for the first word. Every time we 
# find an occurrence of the first word, we search the entire array for the closest occurrence of the second word.

from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDistance = len(wordsDict)
        for i in range(len(wordsDict)):
            if word1 == wordsDict[i]:
                for j in range(len(wordsDict)):
                    if word2 == wordsDict[j]:
                        minDistance = min(minDistance, abs(i-j))
        return minDistance


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
obj = Solution()
print(obj.shortestDistance(wordsDict, word1, word2))


# Complexity analysis:
# Time complexity : O(n^2), since for every occurrence of word1, we traverse the entire array in search for the 
# closest occurrence of word2.
# Space complexity : O(1), since no additional space is used.
