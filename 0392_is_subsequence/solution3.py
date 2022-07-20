# Approach 3: Greedy Match with Character Indices Hashmap
# https://leetcode.com/problems/is-subsequence/solution/

# for follow-up question:
# If there are lots of incoming S, say S_1, S_2, ..., and you want to check one by one to see if T has its 
# subsequence. In this scenario, how would you change your code?

# In the above scenario, we would expect several incoming source strings, but a constant target string. We are 
# asked to match each of the source strings against the target string.
# If we apply our previous algorithms, for each match, the overall time complexity would be O(∣T∣).
# In other words, regardless of the source strings, in the worst case, we have to scan the target string 
# repeatedly, even though the target string remains the same.

# The reason why we scan the target string is to look for the next character that matches a given character in the 
# source string. In essence, this is a lookup operation in the array data structure.
# To speed up the lookup operation, the data structure of hashmap could come in handy, since it has a O(1) time 
# complexity for its lookup operation. Indeed, we could build a hashmap out of the target string, with each unique 
# character as key and the indices of its appearance as value.
# Moreover, we should pre-compute this hashmap once and then reuse it for all the following matches.

# Algorithm:
# - First, we build a hashmap out of the target string. Each key is a unique character in the target string, 
#   e.g. a. Its corresponding value would be a list of indices where the character appears in the target 
#   string, e.g. [0, 3].
# - We then iterate through the source string.
# - This time, rather than keeping two pointers, we need only one pointer on the target string. The pointer marks 
#   our progress on the target string.
# - As we've seen from all the previous approaches, the pointer on the target string should move monotonically, 
#   i.e. in no case, we would move the pointer to an earlier position.
# - We use the pointer to check if an index is suitable or not. For instance, for the character 'a' whose 
#   corresponding indices are [0, 3], we need to pick an index out of all the appearances as a match. Suppose at 
#   certain moment, the pointer is located at the index 1. Then, the suitable greedy match would be the index of 
#   3, which is the first index that is larger than the current position of the target pointer.

# https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
# O(log(n)) -> Bisect method works on the concept of binary search


import bisect
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

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


# OR
# greedy match with linear search, instead of using bisect function(binary search).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

        curr_match_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False  # no match at all, early exit
            
            is_matched = False
            # greedy match with linear search
            for match_index in letter_indices_table[letter]:
                if curr_match_index < match_index:
                    curr_match_index = match_index
                    is_matched = True
                    break
            if not is_matched:
                return False
            
        # consume all characters in the source string
        return True


s = "abc"
t = "ahbgdc"
obj = Solution()
print(obj.isSubsequence(s, t))


# Optimization:
# As one might notice, we added a last touch to the above algorithm to make it faster.
# Given a list of indices for a matched character, in order to find the suitable index, we could simply do the 
# linear search. Since the list of indices is ordered, due to the process of construction, we could also apply the 
# binary search on the list to locate the desired index faster.

# Complexity Analysis:
# Let |S| be the length of the source string, and |T| be the length of the target string.
# Time complexity : O( ∣T∣ + ∣S∣ ⋅ log∣T∣ ).
# - First of all, we build a hashmap out of the target string, which would take O(∣T∣) time complexity. But if we 
#   redesign the API to better fit the scenario of the follow-up question, we should put the construction of the 
#   hashmap in the constructor of the class, which should be done only once.
# - As the second part of the algorithm, we scan through the source string, and lookup the corresponding indices 
#   in the hashmap. The lookup operation in hashmap is constant. However, to find the suitable index would take 
#   either O(∣T∣) with the linear search or O(log∣T∣) with the binary search. To summarize, this part would be 
#   bounded by O(∣S∣ ⋅ log∣T∣).  
# Space complexity : O(∣T∣).
# - We built a hashmap that consists of the indices for each character in the target string. Hence, the size of 
#   values (indices) in hashmap would be |T|. In the worst case, we might have as many keys as the values, i.e. 
#   each character corresponds to a unique index. In total, the space complexity of the hashmap would be O(∣T∣).