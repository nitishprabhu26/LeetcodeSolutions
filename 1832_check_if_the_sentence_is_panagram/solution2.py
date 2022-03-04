# Approach: using dict and set

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict = {}
        
        for i in sentence:
            dict[i] = dict.get(i, 0) + 1
        return len(dict) == 26   

# Complexity Analysis:
# Time complexity: O(n), n is the length of input
# Space complexity: O(1), since dict contains max of 26 characters


# OR


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


# Complexity Analysis:
# Time O(n)
# set. add() function is O(1) because Python's set data structure is implemented as a hash table and you can 
# expect lookup, insert, and delete operations to have constant runtime complexity.
# but here internal for loop runs, having a length of input 'n'
# Space O(26)


sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "leetcode"
obj = Solution()
print(obj.checkIfPangram(sentence))

