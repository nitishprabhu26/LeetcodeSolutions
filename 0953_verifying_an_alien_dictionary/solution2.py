# Approach: Using arrays
# https://youtu.be/jK5a8T9q4pc


from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = [0] * 26
        seq = 0
        
        for ch in order:
            mapping[ord(ch) - ord('a')] = seq
            seq += 1

        for i in range(len(words) - 1):
            curr_word = words[i]
            next_word = words[i + 1]
            
            # take minimum of the lendths, and loop till that point
            min_len = min(len(curr_word), len(next_word))
            
            # for the case: when words are like (curr_word = "apple", next_word = "app").
            # when length of second word is lesser
            if min_len != len(curr_word) and min_len == len(next_word) and curr_word.startswith(next_word):
                return False
            
            for j in range(min_len):
                if mapping[ord(curr_word[j]) - ord('a')] > mapping[ord(next_word[j]) - ord('a')]:
                    return False
                
                if mapping[ord(curr_word[j]) - ord('a')] < mapping[ord(next_word[j]) - ord('a')]:
                    break
                                    
        return True
        

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
obj = Solution()
print(obj.isAlienSorted(words, order))


# Complexity Analysis:
# Let N be the length of order, and M be the total number of characters in words.(not number of words)
# Time complexity: O(M).
# Space complexity: O(1).