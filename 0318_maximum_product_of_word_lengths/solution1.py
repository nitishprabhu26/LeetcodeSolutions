# https://leetcode.com/problems/maximum-product-of-word-lengths/solution/

# The number of operations performed in the nested loops is
# (N - 1) + (N - 2) + ... + 2 + 1 = N(N−1)/2
# that results in O(N^2 * f(L_1, L_2)) time complexity. 
# Here f(L_1, L_2) is a complexity of function noCommonLetters(String s1, String s2), i.e. the price to compare 
# two words of lengths L_1 and L_2.


# Approach 1: Optimize noCommonLetters function : Bitmasks + Precomputation
# The idea is to minimize first the time complexity f(L_1, L_2) of word comparison.


# 1. Naive Solution : O(L_1 * L_2) time
# This naive solution is simple but not optimal. Check the characters in the first word one by one. For each 
# character ensure that this character is not in the second word.

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def no_common_letters(s1, s2):
            for ch in s1:
                if ch in s2:
                    return False
            return True
            
        n = len(words)
        max_prod = 0
        for i in range(n):
            for j in range(i + 1, n):
                if no_common_letters(words[i], words[j]):
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
        return max_prod
        


# 2. Bitmasks : O(L_1 + L_2) time [Time Limit Exceeded ??]
# More elegant and fast solution would be to use bitmasks.
# Words contain only lower case letters and hence an absence or presence of each letter in a word could be encoded 
# with a bitmask of 26 elements. Let's set bit number 0 equal to 1 if character 'a' is present in the word, and to 
# 0 otherwise. And so on and so forth, till the bit number 26 which is equal to 1 if z is present in the word.

# How to set n-th bit? Use standard bitwise trick : n_th_bit = 1 << n.
# How to compute bitmask for a word? Iterate over the word, letter by letter, compute bit number corresponding to 
# that letter n = (int)ch - (int)'a', and add this n-th bit, n_th_bit = 1 << n into bitmask bitmask |= n_th_bit.

# This way one could compute two bitmasks, character by character, in O(L_1 + L_2) time. Then the word comparison 
# itself could be done in one operation and in a constant time.


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def no_common_letters(s1, s2):
            bit_number = lambda ch : ord(ch) - ord('a')

            bitmask1 = bitmask2 = 0
            for ch in s1:
                bitmask1 |= 1 << bit_number(ch)
            for ch in s2:
                bitmask2 |= 1 << bit_number(ch)
            return bitmask1 & bitmask2 == 0
            
        n = len(words)
        max_prod = 0
        for i in range(n):
            for j in range(i + 1, n):
                if no_common_letters(words[i], words[j]):
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
        return max_prod



# 3. Bitmasks + Precomputation : Comparison in O(1) time
# In the previous approach one computes a bitmask of each word N times. In fact, each bitmask could be precomputed 
# just once, memorised and then used for the runtime comparison in a constant time. Let's use two integer arrays 
# to store bitmasks and string lengths.

# Algorithm:
# - Precompute bitmasks for all words and save them in the array masks. Use array lens to keep the lengths for all 
#   words.
# - Compare each word with all the following words one by one. If two words have no common letters, update the 
#   maximum product maxProd. Perform "no common letters" check in a constant time with the help of precomputed 
#   masks array: (masks[i] & masks[j]) == 0.
# - Return maxProd.


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n
        bit_number = lambda ch : ord(ch) - ord('a')
        
        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                # add bit number bit_number in bitmask
                bitmask |= 1 << bit_number(ch)
            masks[i] = bitmask
            lens[i] = len(words[i])
            
        max_val = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    max_val = max(max_val, lens[i] * lens[j])
        return max_val



words = ["abcw","baz","foo","bar","xtfn","abcdef"]
obj = Solution()
print(obj.maxProduct(words))


# Complexity Analysis:
# Time complexity : O(N^2 +L) where N is a number of words and L is a total length of all words together. The 
# precomputation takes O(L) time because we iterate over all characters in all words. The runtime word comparison 
# takes O(N^2). In total, that results in O(N^2 + L) time complexity.
# Space complexity : O(N) to keep two arrays of N elements.