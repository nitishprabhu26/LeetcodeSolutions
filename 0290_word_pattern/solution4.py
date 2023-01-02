# Approach 2: Single Index Hash Map
# https://leetcode.com/problems/word-pattern/solution/


# Intution:
# Rather than having two hash maps, we can have a single index hash map which keeps track of the first occurrences 
# of each character in pattern and each word in s. As we go through each character-word pair, we insert unseen 
# characters from pattern and unseen words from s.
# The goal is to make sure that the indices of each character and word match up. As soon as we find a mismatch, we 
# can return False.

# Let's go through some examples.

# pattern: 'abba'
# s: 'dog cat cat dog'
# 1. 'a' and 'dog' -> map_index = {'a': 0, 'dog': 0}
#       Index of 'a' and index of 'dog' are the same.
# 2. 'b' and 'cat' -> map_index = {'a': 0, 'dog': 0, 'b': 1, 'cat': 1}
#       Index of 'b' and index of 'cat' are the same.
# 3. 'b' and 'cat' -> map_index = {'a': 0, 'dog': 0, 'b': 1, 'cat': 1}
#       'b' is already in the mapping, no need to update.
#       'cat' is already in the mapping, no need to update.
#       Index of 'b' and index of 'cat' are the same.
# 4. 'a' and 'dog' -> map_index = {'a': 0, 'dog': 0, 'b': 1, 'cat': 1}
#       'a' is already in the mapping, no need to update.
#       'dog' is already in the mapping, no need to update.
#       Index of 'a' and index of 'dog' are the same.

# pattern: 'abba'
# s: 'dog cat fish dog'
# 1. 'a' and 'dog' -> map_index = {'a': 0, 'dog': 0}
#       Index of 'a' and index of 'dog' are the same.
# 2. 'b' and 'cat' -> map_index = {'a': 0, 'dog': 0, 'b': 1, 'cat': 1}
#       Index of 'b' and index of 'cat' are the same.
# 3. 'b' and 'fish' -> map_index = {'a': 0, 'dog': 0, 'b': 1, 'cat': 1, 'fish': 2}
#       'b' is already in the mapping, no need to update.
#       Index of 'b' and index of 'fish' are NOT the same. Returns False.

# Implementation:
# Differentiating between character and string: In Python there is no separate char type. And for cases such as:
# pattern: 'abba'
# s: 'b a a b'
# Using the same hash map will not work properly. A workaround is to prefix each character in pattern with "char_" 
# and each word in s with "word_".


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in map_index:
                map_index[char_key] = i
            
            if char_word not in map_index:
                map_index[char_word] = i 
            
            if map_index[char_key] != map_index[char_word]:
                return False
        
        return True


pattern = "abba"
s = "dog cat cat dog"
obj = Solution()
print(obj.wordPattern(pattern, s))


# Complexity Analysis:
# Time Complexity: O(N) where N represents the number of words in s or the number of characters in pattern.
# Space Complexity: O(M) where M is the number of unique characters in pattern and words in s.

