# Approach: Same as Approach 1
# https://youtu.be/ByQfvU8_fvM

# Intuition:
# For example, when checking whether "warrior" is a superset of words B = ["wrr", "wa", "or"], we can combine 
# these words in B to form a "maximum" word "arrow", that has the maximum count of every letter in each word in B.

# Algorithm:
# Reduce B to a single word bmax as described above, then compare the counts of letters between words a in A, and 
# bmax.


from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def isSubset(src, dest):
            for i in range(26):
                if dest[i] > src[i]:
                    return False
            return True
            
        ans = []
        bmax = [0] * 26
        
        # to find bmax
        for b in words2:
            temp = [0] * 26    
            for letter in b:
                temp[ord(letter) - ord('a')] += 1
                bmax[ord(letter) - ord('a')] = max(bmax[ord(letter) - ord('a')], temp[ord(letter) - ord('a')])
        
        for a in words1:
            arr = [0] * 26
            for letter in a:
                arr[ord(letter) - ord('a')] += 1
                
            if isSubset(arr, bmax):
                ans.append(a)
                
        return ans
        

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
obj = Solution()
print(obj.wordSubsets(words1, words2))


# Complexity Analysis:
# Time Complexity: O(A + B), where A and B is the total amount of information in A and B respectively.
# Space Complexity: O(A.length + B.length).

