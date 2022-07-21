# Approach #1: Brute Force [Time Limit Exceeded]
# https://www.geeksforgeeks.org/python-iter-method/
# https://www.geeksforgeeks.org/python-all-function/

# Intuition and Algorithm:
# Let's try to check separately whether each word words[i] is a subsequence of S.
# For every such word, we try to find the first occurrence of word[0] in S, then from that point on try to find
# the first occurrence of word[1], and so on.


from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def subseq(word):
            it = iter(s)
            # doesnt work for: 
            # it = list(s)
            # because StopIteration exception is raised incase of iter()
            return all(x in it for x in word)

        return sum(subseq(word) for word in words)


s = "abcde"
words = ["a","bb","acd","ace"]
obj = Solution()
print(obj.numMatchingSubseq(s, words))


# Complexity Analysis:
# Time Complexity: O(words.length ∗ S.length + ∑i words[i].length). For each word, our subseq check on word,
# words[i] may take time complexity O(S.length + words[i].length).
# Space Complexity: O(1). (In Java, our space complexity is O(S.length + max(words[i].length)), but can be made to
# be O(1) with a pointer based implementation.)