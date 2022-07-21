# Approach: using the solution from problem 392: Greedy Match with Character Indices Hashmap


import bisect
from collections import defaultdict
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(s):
            letter_indices_table[letter].append(index)
            
        def isSubsequence(s, t) -> bool:
            curr_match_index = -1
            for letter in s:
                if letter not in letter_indices_table:
                    return False  # no match at all, early exit

                # greedy match with binary search
                indices_list = letter_indices_table[letter]
                match_index = bisect.bisect_right(indices_list, curr_match_index)
                if match_index != len(indices_list):
                    curr_match_index = indices_list[match_index]
                else:
                    return False # no suitable match found, early exist

            return True

        return sum(isSubsequence(word, s) for word in words)


s = "abcde"
words = ["a","bb","acd","ace"]
obj = Solution()
print(obj.numMatchingSubseq(s, words))
