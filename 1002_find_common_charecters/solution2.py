# Approach : without using any library functions
# https://leetcode.com/problems/find-common-characters/discuss/332733/Python-Solution-Easy-to-Understand


from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # taking the first word, finding common letters while looping throgh rest of the words
        common = list(words[0])
        
        for word in words[1:]:
            # common letter list keeps getting updated
            newCommon = []
            for c in word:
                if c in common:
                    common.remove(c)
                    newCommon.append(c)
            common = newCommon
        
        return common


# OR similar 
# https://leetcode.com/problems/find-common-characters/discuss/422308/Python-7-lines-beats-100-and-100-in-O(n)

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2 : 
            return list(words[0])
        
        # make a set from first string
        wordList = set(words[0])
        
        res = []
        for one in wordList:
            # count min frequency of every letter in every word
            n = min([a_word.count(one) for a_word in words]) 
            # if n>0 , we append this letter n times
            if n:    
                res += [one]*n
                
        return res
                

words = ["bella","label","roller"]
obj = Solution()
print(obj.commonChars(words))


# Complexity Analysis:
# Time complexity: O(n^3) upper bound.