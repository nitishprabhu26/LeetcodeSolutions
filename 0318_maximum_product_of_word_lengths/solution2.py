# https://leetcode.com/problems/maximum-product-of-word-lengths/solution/

# Approach 2: Optimise Number of Comparisons : Bitmasks + Precomputation + Hashmap
# Now, when the comparison itself is optimised, one could optimise the number of comparisons. There is no need to 
# always perform O(N^2) comparisons. 
# Among all the strings with the same set of letters (abab, aaaaabaabaaabbaaaaabaabaaabb, bbabbabbabbabbabba) it's 
# enough to keep the longest one (aaaaabaabaaabbaaaaabaabaaabb).
# For that, instead of two arrays of length N as in the Approach 1, one could use a hashmap : bitmask -> max word 
# length with that bitmask.
# eg: leetcode and ltcode have the same bitmask (in expamle shown on website)
# This way the total number of word comparisons could be reduced, that speeds up the solution in Python

# Algorithm:
# - Precompute bitmasks for all words and save them in the hashmap, bitmask -> max word length with such a bitmask.
#   (There could be several words with the same bitmask, for example, "a" and "aaaaaaa").
# - Compare each word with all the following words one by one. If two words have no common letters, update the 
#   maximum product maxProd. Perform "no common letters" check in a constant time with the help of precomputed 
#   hashmap of bitmasks: (x & y) == 0.
# - Return maxProd.


from typing import List
from collections import defaultdict

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        hashmap = defaultdict(int)
        bit_number = lambda ch : ord(ch) - ord('a')
        
        for word in words:
            bitmask = 0
            for ch in word:
                # add bit number bit_number in bitmask
                bitmask |= 1 << bit_number(ch)
            # there could be different words with the same bitmask
            # ex. ab and aabb
            hashmap[bitmask] = max(hashmap[bitmask], len(word))

        max_prod = 0
        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    max_prod = max(max_prod, hashmap[x] * hashmap[y])
        return max_prod
        

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
obj = Solution()
print(obj.maxProduct(words))


# Complexity Analysis:
# Time complexity : O(N^2 +L) where N is a number of words and L is a total length of all words together.
# Space complexity : O(N) to keep a hashmap of N elements if N < 2^26. Otherwise, it's O(2^26) = O(1).