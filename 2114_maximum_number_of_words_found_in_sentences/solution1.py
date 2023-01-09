# Approach: Using inbuilt split function


from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sentence in sentences:
            words = sentence.split(' ')
            res = max(res, len(words))
        
        return res

# OR

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
	    return max(len(word.split()) for word in sentences)


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
obj = Solution()
print(obj.mostWordsFound(sentences))


# Complexity Analysis:
# Time complexity : O(M * N), where M is the number of sentences and N is the max number of words 
# in one of the sentences.
# Space complexity : O(M * N).