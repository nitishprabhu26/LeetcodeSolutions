# Approach: IN operator or Find

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        
        for char in alphabets:
            if char not in sentence:
                return False
        return True

# OR

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        alphaSet = set(alphabets)
        for char in alphaSet:
            if char not in sentence:
                return False
        return True

# OR

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        
        for char in alphabets:
            if sentence.find(char) == -1:
                return False
        return True


sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "leetcode"
obj = Solution()
print(obj.checkIfPangram(sentence))


# Complexity Analysis:
# Time complexity: O(n) using 'in' function, for loop - O(26) i.e. O(1)
# list, string - Average: O(n)
# set/dict - Average: O(1), Worst: O(n)
# Space complexity: O(n), n is the length of input