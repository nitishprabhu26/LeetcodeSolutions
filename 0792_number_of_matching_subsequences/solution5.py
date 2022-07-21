# Approach #2: Next Letter Pointers [Accepted]
# for explaination(intuition): https://leetcode.com/problems/number-of-matching-subsequences/solution/ 
# OR
# code: https://leetcode.com/problems/number-of-matching-subsequences/discuss/329381/Python-Solution-With-Detailed-Explanation

# Algorithm:
# - Begin by creating a default dictionary of 'list' objects. The main benefit of a default dictionary is that when 
#   you access an entry that does not yet exist, the entry is created automatically (in this case, the value for 
#   the entry is an empty list when it is created). 
# - Create a 'count' variable to keep track of the number of words that are subsequences of the given string.
# - Populate dictionary with all the words in the list of words. The key for each entry is the first letter of the 
#   word. The value is the list of words that start with that letter. Using the example in the problem, the 
#   dictionary would look like the following:
#   {'a': ['a', 'acd', 'ace'], 'b': ['bb']}
# - The next step is to iterate through each character in the given string. 
#   For each character, I access the dictionary to retrieve the list of words that start with that character. 
#   Reset the value of the entry to an empty list and then iterate through the list of words I retrieved. 
#   -   If the word is only a single letter, then I conclude that we have successfully found a completed 
#       subsequence and increase our 'count' by one. 
#   -   Otherwise, slice off the first character and add the sliced word back to the dictionary. This time, it is 
#       added to the entry for which the key is equal to the first letter of the sliced word.
# - This process continues until we have iterated through all characters in the string. At the end, return count.


from collections import defaultdict
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in s:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count


s = "abcde"
words = ["a","bb","acd","ace"]
obj = Solution()
print(obj.numMatchingSubseq(s, words))


# Complexity Analysis:
# Time Complexity: O(S.length + ∑i words[i].length).
# Space Complexity: O(words.length).