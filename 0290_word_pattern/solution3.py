# Addendum: Rather than keeping two hash maps, we can only keep character to word mapping and whenever we find a 
# character that is not in the mapping, you can check whether the word in current character-word pair is already 
# one of the values in the character to word mapping. However, this is trading time off for better space since 
# checking for values in a hash map is a O(M) operation where M is the number of key value pairs in the hash map. 
# Thus, if we decide to go this way, our time complexity will be O(N.M) where N is the number of unique characters 
# in pattern. and O(1) is the space complexity.
# OR
# https://youtu.be/XC0dpyntbyA


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in char_to_word:
                if w in char_to_word.values():
                    return False
                else:
                    char_to_word[c] = w
            else:
                if char_to_word[c] != w:
                    return False
        return True


# Another similar approach to Approach 1 would be using hash set to keep track of words which have been encountered. 
# Instead of checking whether the word is already in the word to character mapping, you just need to check whether 
# the word is in the encountered word hash set. And, rather than updating the word to character mapping, you just 
# need to add the word to the encountered word hash set. Hash set would have a better practical space complexity 
# even though the big-O space complexity for hash set and hash map is the same.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        word_set = set()
        
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in char_to_word:
                if w in word_set:
                    return False
                else:
                    char_to_word[c] = w
                    word_set.add(w)
            else:
                if char_to_word[c] != w:
                    return False
        return True


pattern = "abba"
s = "dog cat cat dog"
obj = Solution()
print(obj.wordPattern(pattern, s))