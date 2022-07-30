# Approach: Brute force[Time Limit Exceeded]
# For every word in A, check if all words in B are A's subsets
# https://youtu.be/ByQfvU8_fvM


from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans
        
        ans = []
        for word1 in words1:
            valid = True
            word1_char_array = count(word1)

            for word2 in words2:
                if all(x >= y for x, y in zip(word1_char_array, count(word2))):
                    valid = True
                else:
                    valid = False
                    
                if not valid:
                    break
            
            # append to result, only if all the strings in words2 are subset of a particular word in words1
            if valid:
                ans.append(word1)
                
        return ans
        

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
obj = Solution()
print(obj.wordSubsets(words1, words2))


# Complexity Analysis:
# Time Complexity: O(m.n), where m and n are lengths of arrays words1 and words2 respectively.
