# Overview:
# To check if the given words are sorted, for each word we need to check if every word on its right is 
# lexicographically larger. Likewise, for each word we could check if every word on its left is lexicographically 
# smaller. That said, we don't need to compare every word to all of the words to its right. Instead, we can just 
# compare each pair of adjacent words. If all pairs of adjacent words are sorted, then we can safely conclude that 
# words is sorted. Furthermore, if any pair of adjacent words is not sorted, then we know that words is not sorted.

# Approach 1: Compare adjacent words

# Algorithm:
# - Initialize a hashmap/array to record the relations between each letter and its ranking in order.
# - Iterate over words and compare each pair of adjacent words.
#   -   Iterate over each letter to find the first different letter between words[i] and words[i + 1].
#       -   If words[i + 1] ends before words[i] and no different letters are found, then we need to return false 
#           because words[i + 1] should come before words[i] (for example, apple and app).
#       -   If we find the first different letter and the two words are in the correct order, then we can exit 
#           from the current iteration and proceed to the next pair of words.
#       -   If we find the first different letter and the two words are in the wrong order, then we can safely 
#           return false.
# - If we reach this point, it means that we have examined all pairs of adjacent words and that they 
#   are all sorted. Therefore we can return true.


from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
obj = Solution()
print(obj.isAlienSorted(words, order))


# Complexity Analysis:
# Let N be the length of order, and M be the total number of characters in words.(not number of words)
# Time complexity: O(M). 
#   -   Storing the letter-order relation of each letter takes O(N) time. For the nested for-loops, we examine 
#       each pair of words in the outer-loop and for the inner loop, we check each letter in the current word. 
#       Therefore, we will iterate over all of letters in words.
#       Taking both into consideration, the time complexity is O(M+N). However, we know that N is fixed as 26. 
#       Therefore, the time complexity is O(M).
#       OR
#   -   Extra:
#       One O(A) iteration to build order, fixed at 26.
#       One O(B) iteration to iterate over words, where B is number of words.
#       One O(C) iteration to iterate over letters; where C is the average characters in words.
#       It makes sense to drop the constant O(A) iteration over 26 chars from complexity analysis. Which leaves us 
#       with O(B * C) time complexity, where B*C = M (i.e. the total number of characters in words).
# Space complexity: O(1).
#   -   The only extra data structure we use is the hashmap/array that serves to store the letter-order relations 
#       for each word in order. Because the length of order is fixed as, this approach achieves constant space 
#       complexity.