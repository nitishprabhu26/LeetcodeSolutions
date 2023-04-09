# Approach: Neetcode
# https://youtu.be/OVgPAJIyX6o


from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # first differing char
        # if word A is prefix of word B, word B must be after word A
        
        overInd = {c : i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            for j in range(len(w1)):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j == len(w2): 
                    return False

                if w1[j] != w2[j]:
                    if overInd[w1[j]] > overInd[w2[j]]: 
                        return False
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