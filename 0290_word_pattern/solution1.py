# Approach 1: Two Hash Maps

# Algorithm:
# Have two hash maps, one for mapping characters to words and the other for mapping words to characters. While 
# scanning each character-word pair:

# - If the character is NOT in the character to word mapping, you additionally check whether that word is also 
#   in the word to character mapping.
#   -   If that word is already in the word to character mapping, then you can return False immediately since 
#       it has been mapped with some other character before.
#   -   Else, update both mappings.
# - If the character IS IN in the character to word mapping, you just need to check whether the current word 
#   matches with the word which the character maps to in the character to word mapping. If not, you can 
#   return False immediately.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_char = {}
        map_word = {}
        
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True

pattern = "abba"
s = "dog cat cat dog"
obj = Solution()
print(obj.wordPattern(pattern, s))

# Complexity Analysis
# Time Complexity: O(N) where N represents the number of words in s or the number of characters in pattern.
# Space Complexity :  O(M) where M represents the number of unique words in s. Even though we have two hash 
# maps, the character to word hash map has space complexity of O(1) since there can at most be 26 keys.

