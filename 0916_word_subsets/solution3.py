# Approach 1: Reduce to Single Word in B

# Intuition:
# For example, when checking whether "warrior" is a superset of words B = ["wrr", "wa", "or"], we can combine 
# these words in B to form a "maximum" word "arrow", that has the maximum count of every letter in each word in B.

# Algorithm:
# Reduce B to a single word bmax as described above, then compare the counts of letters between words a in A, and 
# bmax.


from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in words2:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in words1:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans
        

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
obj = Solution()
print(obj.wordSubsets(words1, words2))


# Complexity Analysis:
# Time Complexity: O(A + B), where A and B is the total amount of information in A and B respectively.
# Space Complexity: O(A.length + B.length).
